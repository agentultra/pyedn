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

    def test_two_nil(self):
        in_string = u"nil nil"
        out = lexer.lex(in_string)
        self.assertTrue(out)
        self.assertEqual(len(out), 2)
        self.assertEqual(out[0].text, out[1].text)
        self.assertEqual(out[0].tag, out[1].tag)
        self.assertEqual(out[0].position, 0)
        self.assertEqual(out[1].position, 4)

    def test_two_nil_with_comma(self):
        in_string = u"nil,nil"
        out = lexer.lex(in_string)
        self.assertTrue(out)
        self.assertEqual(len(out), 2)
        self.assertEqual(out[0].text, out[1].text)
        self.assertEqual(out[0].tag, out[1].tag)
        self.assertEqual(out[0].position, 0)
        self.assertEqual(out[1].position, 4)

    def test_boolean(self):
        in_string = u"true false"
        out = lexer.lex(in_string)
        self.assertTrue(out)
        self.assertEqual(len(out), 2)
        self.assertEqual(out[0].text, "true")
        self.assertEqual(out[1].text, "false")
        self.assertEqual(out[0].tag, "BOOL")

    def test_string(self):
        in_string = u"\"foo, bar baz!\""
        out = lexer.lex(in_string)
        self.assertTrue(out)
        self.assertEqual(len(out), 1)
        self.assertEqual(out[0].text, u"\"foo, bar baz!\"")
        self.assertEqual(out[0].tag, "STRING")

    def test_escape_characters_in_string(self):
        in_string = u"\"foo, bar\nbaz!!\""
        out = lexer.lex(in_string)
        self.assertTrue(out)
        self.assertEqual(len(out), 1)
        self.assertEqual(out[0].text, u"\"foo, bar\nbaz!!\"")
        self.assertEqual(out[0].tag, "STRING")

    def test_character(self):
        in_string = u"\c"
        out = lexer.lex(in_string)
        self.assertTrue(out)
        self.assertEqual(len(out), 1)
        self.assertEqual(out[0].text, "\c")
        self.assertEqual(out[0].tag, "CHAR")

    def test_characters(self):
        in_string = u"\\h \\e \\l \\l \\o \\space \\w \\o \\r \\l \\d"
        out = lexer.lex(in_string)
        self.assertEqual(len(out), 11)
