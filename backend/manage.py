#!/usr/bin/env python
from copy import deepcopy
from datetime import datetime, date, timedelta
import json
from glob import glob
import gzip
from hashlib import sha1
import os
import sys
import time
import logging
from time import sleep
import glob
import csv
from pprint import pprint
import re

import translitcodec
import requests
import click
from click.core import Command
from click.decorators import _make_command
from elasticsearch.exceptions import NotFoundError
from elasticsearch.helpers import bulk

from openlobby.utils import load_config, slugify
from openlobby.es import setup_elasticsearch

logging.basicConfig(
    format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d:%(message)s',
    level=logging.INFO)

def command(name=None, cls=None, **attrs):
    """
    Wrapper for click Commands, to replace the click.Command docstring with the
    docstring of the wrapped method (i.e. the methods defined below). This is
    done to support the autodoc in Sphinx, and the correct display of docstrings
    """
    if cls is None:
        cls = Command
    def decorator(f):
        r = _make_command(f, name, attrs, cls)
        r.__doc__ = f.__doc__
        return r
    return decorator


def _create_path(path):
    if not os.path.exists(path):
        click.secho('Creating path "%s"' % path, fg='green')
        os.makedirs(path)

    return path


def extract_organizations(rows):
    result = {
        "tweede-kamer": {
            "_id": "tweede-kamer",
            "_index": "openlobby_organizations",
            "id": "tweede-kamer",
            "name": "Tweede Kamer",
            "classification": "Tweede Kamer",
            "description": "Tweede Kamer der Staten Generaal"
        }
    }
    for r in rows:
        org = r['ORGNAAM'].strip()
        org_type = r['ORGTYPE'].strip()
        org_slug = slugify(org)
        if (org == '') or (org_slug in result):
            continue
        result[org_slug] = {
            "_id": org_slug,
            "_index": "openlobby_organizations",
            "id": org_slug,
            "name": org,
            "classification": r['ORGTYPE'],
            "description": r['ORGTYPE']
        }
    return result


def extract_persons(rows, orgs, parties):
    result = {}
    last_row = None
    for r in rows:
        per = r['PERSOON'].strip()
        org = r['PARTIJ'].strip()
        if (per != '') and (org != ''):
            last_row = r
        if (per == '') and (org == '') and (last_row is not None):
            per = last_row['PERSOON'].strip()
            org = last_row['PARTIJ'].strip()
        per_slug = slugify(per)
        org_slug = slugify(org)
        org = r['ORGNAAM'].strip()
        org_type = r['ORGTYPE'].strip()
        org_slug = slugify(org)

        year = ''
        matches = re.search('(\d{4})$', r['BEGINANDERS'])
        if matches:
            year = matches.group(1)

        membership = {
            "organization_id": org_slug,
            "role": r['VOLGENDEFUNCTIE']
        }
        if year != '':
            membership["start_date"] = '%s-01-01' % (year)

        if per_slug not in result:
            chamber_membership = {
                "organization_id": "tweede-kamer",
                "organization": orgs['tweede-kamer'],
                "label": "functie",
                "role": 'Kamerlid'
            }
            begin_lid = r['BEGINLID'].strip()
            if begin_lid != '':
                chamber_membership["start_date"] = "%s-01-01" % (
                    begin_lid)
            result[per_slug] = {
                "_id": per_slug,
                "_index": "openlobby_persons",
                "id": per_slug,
                "name": per,
                "description": r['NEVENFUNCTIES'].strip(),
                "memberships": [chamber_membership]
            }
        if org != '':
            membership["organization"] = orgs[org_slug]
            result[per_slug]["memberships"].append(membership)

    return result


def extract_parties(rows):
    result = {}
    for r in rows:
        org = r['PARTIJ'].strip()
        org_slug = slugify(org)
        if (org == '') or (org_slug in result):
            continue
        result[org_slug] = {
            "_id": org_slug,
            "_index": "openlobby_organizations",
            "id": org_slug,
            "name": org,
            "classification": "Politieke partij",
            "description": ""
        }
    return result


@click.group()
@click.version_option()
def cli():
    """Open Lobby"""


@cli.group()
def elasticsearch():
    """Manage Elasticsearch"""


@command('put_templates')
@click.option('--template_dir', default='./mappings/', help='Path to JSON file containing the template.')
def es_put_template(template_dir):
    """
    Put a template into Elasticsearch. A template contains settings and mappings
    that should be applied to multiple indices. Check ``mappings/template.json``
    for an example.
    :param template_file: Path to JSON file containing the template. Defaults to ``mappings/template.json``.
    """

    config = load_config()
    es = setup_elasticsearch(config)

    click.echo('Putting ES template from dir: %s' % template_dir)

    for template_path in glob.glob(os.path.join(template_dir, 'es-*.json')):
        click.echo(template_path)
        template = {}
        with open(template_path, 'rb') as template_file:
            template = json.load(template_file)
        template_name = os.path.basename(template_file.name.replace('es-','').replace('.json', ''))
        es.indices.put_template(template_name, template)
        index_name = 'openlobby_%s' % (template_name)
        if not es.indices.exists(index=index_name):
            click.echo("Should make index %s" % (index_name,))
            es.indices.create(index=index_name)


@command('load')
@click.option('--data_file', default='data/test.json',
              type=click.File('rb'), help='Path to JSON file containing the data.')
def es_load(data_file):
    """
    Loads data into Elasticsearch. A file needs to be given containing the data.
    :param data_file: Path to JSON file containing the data. Defaults to ``data/test.json``.
    """
    config = load_config()
    es = setup_elasticsearch(config)
    data = json.load(data_file)
    result = bulk(es, data, False)


@command('load_csv')
@click.option('--data_file', default='data/tk-2012-2021.csv',
              type=click.File('r'), help='Path to CSV file containing the data.')
def es_load_csv(data_file):
    """
    Loads data into Elasticsearch. A file needs to be given containing the data.
    :param data_file: Path to JSON file containing the data. Defaults to ``data/test.json``.
    """
    reader = csv.DictReader(data_file)
    rows = []
    for row in reader:
        rows.append(row)
        pprint(row)
    orgs = extract_organizations(rows)
    #pprint(orgs)
    parties = extract_parties(rows)
    #pprint(parties)
    persons = extract_persons(rows, orgs, parties)
    #pprint(persons)
    pprint(persons["arno-rutte"])
    pprint(orgs['vintura'])
    pprint(persons["wybren-van-haga"])
    # pprint(persons["martijn-bolkestein"])
    # print(orgs["tweede-kamer"])
    config = load_config()
    es = setup_elasticsearch(config)
    data = list(orgs.values()) + list(parties.values()) + list(persons.values())
    result = bulk(es, data, False)

# Register commands explicitly with groups, so we can easily use the docstring
# wrapper
elasticsearch.add_command(es_put_template)
elasticsearch.add_command(es_load)
elasticsearch.add_command(es_load_csv)

if __name__ == '__main__':
    cli()
