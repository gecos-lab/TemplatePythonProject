# Standard library imports
import os

# Third party imports
import opengeode


# Local application imports


def sum(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def load_brep(filename):
    path = os.path.join(os.path.dirname(__file__), filename)
    return opengeode.load_brep(path)
