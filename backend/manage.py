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

import requests

import click
from click.core import Command
from click.decorators import _make_command
from elasticsearch.exceptions import NotFoundError
from elasticsearch.helpers import bulk

from openlobby.utils import load_config
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


# Register commands explicitly with groups, so we can easily use the docstring
# wrapper
elasticsearch.add_command(es_put_template)
elasticsearch.add_command(es_load)

if __name__ == '__main__':
    cli()
