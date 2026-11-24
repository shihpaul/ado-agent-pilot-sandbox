import unittest

from whitespace import normalize_whitespace


class NormalizeWhitespaceTests(unittest.TestCase):
    def test_normal_text(self):
        self.assertEqual(normalize_whitespace("a short sentence"), "a short sentence")

    def test_repeated_ascii_spaces(self):
        self.assertEqual(normalize_whitespace("  first   second    "), "first second")

    def test_tabs(self):
        self.assertEqual(normalize_whitespace("\tone\t\ttwo\t"), "one two")

    def test_newlines(self):
        self.assertEqual(normalize_whitespace("\nfirst\r\n\nsecond\r"), "first second")

    def test_unicode_whitespace(self):
        text = "\u00a0one\u2003\u202ftwo\u2028three\u3000"
        self.assertEqual(normalize_whitespace(text), "one two three")

    def test_mixed_whitespace(self):
        text = " \t\u00a0first\r\n \u2003\v\fsecond\u0085\t "
        self.assertEqual(normalize_whitespace(text), "first second")

    def test_whitespace_control_characters(self):
        text = "\x1cfirst\x1d\x1esecond\x1f"
        self.assertEqual(normalize_whitespace(text), "first second")

    def test_empty_string(self):
        self.assertEqual(normalize_whitespace(""), "")

    def test_whitespace_only(self):
        self.assertEqual(normalize_whitespace(" \t\r\n\u00a0\u2003\u3000"), "")

    def test_non_ascii_text(self):
        self.assertEqual(normalize_whitespace("  café\u3000東京\t🙂  "), "café 東京 🙂")

    def test_punctuation(self):
        self.assertEqual(normalize_whitespace(" Hi,\t world!  (Again?) "), "Hi, world! (Again?)")

    def test_preserves_non_whitespace_characters(self):
        text = "\ufeffe\u0301\u200b\u200d\x00"
        self.assertEqual(normalize_whitespace(f"\t{text}\u00a0"), text)

    def test_accepts_string_subclasses(self):
        class StringSubclass(str):
            pass

        self.assertEqual(normalize_whitespace(StringSubclass("  a\tb ")), "a b")

    def test_rejects_non_string_inputs(self):
        for value in (None, 0, 2.5, 1j, False, b"text", ["text"], ("text",), {}, object()):
            with self.subTest(value=value):
                with self.assertRaises(TypeError):
                    normalize_whitespace(value)

# Synthetic reviewer-trigger fixture: test behavior unchanged.
