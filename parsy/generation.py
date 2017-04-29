# coding: utf-8


"""
Code generation from an expression to a database language.

The currently supported languages are:
    * MQL
    * Sparql
    * Dot: generation of graph images mainly for debugging.
"""

from parsy.mql_generation import generate_mql
from parsy.dot_generation import expression_to_dot
from parsy.sparql_generation import expression_to_sparql


def get_code(expression, language):
    """
    Given an expression and a supported language, it
    returns the query for that expression on that language.
    """

    if language == "sparql":
        return expression_to_sparql(expression)
    elif language == "dot":
        return expression_to_dot(expression)
    elif language == "mql":
        return generate_mql(expression)
    else:
        message = u"Language '{}' is not supported"
        raise ValueError(message.format(language))
