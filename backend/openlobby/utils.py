from yaml import load
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader

import re
import codecs

from openlobby.exceptions import ConfigurationError


def load_config(config_file='config.yaml'):
    """
    Loads a configuration file (which is a YAML file). The location iof the
    file can be specified using the parameter. It further checks if it is a
    valid configuration file and if so, returns the parsed data strcture.
    """
    config = {}
    with open(config_file) as f:
        config = load(f, Loader=Loader)

    if not is_valid_config(config):
        raise ConfigurationError('Not a valid configuration file')

    return config


def is_valid_config(config):
    """
    Checks if a data structure can be considered as a valid binoas
    configuration file. Returns true or false.
    """
    return (
        len(config.keys()) == 1 and
        ('openlobby' in config)
    )

_punct_re = re.compile(r'[\t\r\n !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.]+')

def slugify(text, delim='-'):
    """Generates an ASCII-only slug."""
    result = []
    for word in _punct_re.split(str(text).lower()):
        word = codecs.encode(word, 'translit/long')
        if word:
            result.append(word)
    return delim.join(result)
