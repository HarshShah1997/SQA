# coding: utf-8

"""
Parsy converts Natural Language Question to database queries.
"""

VERSION = 0.2

import logging
from parsy.quepyapp import install, QuepyApp


def set_loglevel(level=logging.WARNING):
    logger = logging.getLogger("quepy")
    logger.setLevel(level)
