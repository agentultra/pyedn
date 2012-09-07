import re
import sys

from collections import namedtuple


Token = namedtuple("Token", "text tag position")


def lex(bytes):
    return [Token("nil", "NIL", 0)]
