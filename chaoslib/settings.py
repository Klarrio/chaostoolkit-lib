# -*- coding: utf-8 -*-
import os
import os.path

from logzero import logger
import yaml

from chaoslib.types import Settings

__all__ = ["load_settings"]
CHAOSTOOLKIT_CONFIG_PATH = os.path.abspath(
    os.path.expanduser("~/.chaostoolkit/settings.yaml"))


def load_settings(settings_path: str=CHAOSTOOLKIT_CONFIG_PATH) -> Settings:
    """
    Load chaostoolkit settings as a mapping of key/values or return `None`
    when the file could not be found.
    """
    if not os.path.exists(settings_path):
        logger.debug("The Chaos Toolkit settings file could not be found at "
                     "'{c}'.".format(c=settings_path))
        return

    with open(settings_path) as f:
        return yaml.load(f.read())
