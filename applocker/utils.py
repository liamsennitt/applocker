import sys

from xml.etree.ElementTree import tostring, fromstring
from applocker.conditions import (
    FilePublisherCondition, # noqa: F401
    FilePathCondition, # noqa: F401
    FileHashCondition, # noqa: F401
)
from applocker.rules import FilePublisherRule, FilePathRule, FileHashRule # noqa: F401
from applocker.policy import AppLockerPolicy # noqa: F401


def dump(element, stream):
    stream.write(dumps(element))


def dumps(element):
    return tostring(element).decode("utf-8")


def load(stream):
    return loads(stream.read())


def loads(string):
    element = fromstring(string)
    return getattr(sys.modules[__name__], element.tag).from_element(element)
