from text_tools import to_upper, to_word_list_isupper
import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual(to_upper('foo'), 'FOO')


    # why did not pass
    def test_word_list_isupper(self):
        self.assertTrue(to_word_list_isupper(['i', 'LOVE', 'PYTHON' ]))


    def test_word_list_isupper(self):
        self.assertFalse(to_word_list_isupper(['i', 'LOVE', 'PYTHON' ]))


if __name__ == '__main__':
    unittest.main()