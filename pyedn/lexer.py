import re
import sys

from collections import namedtuple


Token = namedtuple("Token", "text tag position")
