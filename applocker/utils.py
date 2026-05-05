import sys
from xml.etree.ElementTree import fromstring, tostring

from applocker.conditions import (
    FileHashCondition,  # noqa: F401
    FilePathCondition,  # noqa: F401
    FilePublisherCondition,  # noqa: F401
)
from applocker.policy import AppLockerPolicy  # noqa: F401
from applocker.rules import FileHashRule, FilePathRule, FilePublisherRule  # noqa: F401


def dump(element, stream):
    stream.write(dumps(element))


def dumps(element):
    return tostring(element).decode("utf-8")


def load(stream):
    return loads(stream.read())


def loads(string):
    element = fromstring(string)
    return getattr(sys.modules[__name__], element.tag).from_element(element)
