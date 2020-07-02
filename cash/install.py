#!/usr/bin/env python

from __future__ import print_function, unicode_literals
import xdg.BaseDirectory
import os
import logging
import sys
import json
import yaml
import glob
import copy
from . import api
if "win32" not in sys.platform:
    # readline is not included in Windows Active Python
    import readline

XDG_RESOURCE = 'cash'
DEFAULT_CONFIG_NAME = 'cash.yaml'

USER_HOME = os.path.expanduser('~')
CONFIG_PATH = xdg.BaseDirectory.save_config_path(XDG_RESOURCE) or USER_HOME
CONFIG_FILE_PATH = os.path.join(CONFIG_PATH, DEFAULT_CONFIG_NAME)
CONFIG_FILE_PATH_FALLBACK = os.path.join(USER_HOME, ".cash")

log = logging.getLogger(__name__)
default_config = {'api_key':None, 'default_currency':'USD'}

def load_yaml(config_path):
    """Tries to load a config file from YAML.
    """
    with open(config_path) as f:
        return yaml.load(f, Loader=yaml.FullLoader)

def save_config(config):
    with open(CONFIG_FILE_PATH, 'w') as f:
        yaml.safe_dump(config, f, encoding='utf-8',
                       allow_unicode=True, default_flow_style=False)


def load_or_install():
    config_path = CONFIG_FILE_PATH if os.path.exists(
        CONFIG_FILE_PATH) else CONFIG_FILE_PATH_FALLBACK
    if os.path.exists(config_path):
        log.debug('Reading configuration from file %s', config_path)
        return load_yaml(config_path)
    else:
        log.debug('Configuration file not found, installing jrnl...')
        try:
            config = install()
        except KeyboardInterrupt:
            raise UserAbort("Installation aborted")
        return config


def install():
    if "win32" not in sys.platform:
        readline.set_completer_delims(' \t\n;')
        readline.parse_and_bind("tab: complete")

    path_query = f'api_key (Get one at https://www.currencyconverterapi.com/): '
    default_config['api_key'] = input(path_query).strip() or None

    save_config(default_config)
    return default_config

