import re
import sys

from collections import namedtuple


Token = namedtuple("Token", "text tag position")


NIL = "NIL"
BOOL = "BOOL"
STRING = "STRING"
CHAR = "CHAR"


TOKEN_EXPRS = ((r"[ \n\t,]+", None),
               (r"nil", NIL),
               (r"(true|false)", BOOL),
               (r"\"(?:[^\\\"]+|\\.)*\"", STRING),
               (r"\\[A-Za-z0-9]+", CHAR))


def lex(bytes):
    pos = 0
    tokens = []
    while pos < len(bytes):
        match = None
        for pattern, tag in TOKEN_EXPRS:
            regex = re.compile(pattern)
            match = regex.match(bytes, pos)
            if match:
                text = match.group(0)
                if tag:
                    tokens.append(Token(text, tag, pos))
                break
        if not match:
            raise ValueError("Illegal character {0} in position: {1}\n".format(
                bytes[pos], pos))
        else:
            pos = match.end(0)
    return tokens
