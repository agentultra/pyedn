import unittest

from pyedn import lexer


class TestLexer(unittest.TestCase):

    def test_nil(self):
        in_string = u"nil"
        out = lexer.lex(in_string)
        self.assertTrue(out)
        self.assertEqual(len(out), 1)
        self.assertEqual(out[0].text, "nil")
        self.assertEqual(out[0].tag, "NIL")
        self.assertEqual(out[0].position, 0)
