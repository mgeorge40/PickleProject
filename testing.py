from words_to_number import words_to_number
import unittest

class TestPhoneConversion(unittest.TestCase):

    def test_word2num(self):
        self.assertEqual(words_to_number('1-800-PAINTER'), '1-800-724-6837')
        self.assertEqual(words_to_number('1-800-aa-aba-00'), '1-800-222-2200')
        self.assertEqual(words_to_number('1-800-426-9834'), '1-800-426-9834')
        self.assertEqual(words_to_number('1-800-DOMINOS'), '1-800-366-4667')

if __name__ == '__main__':
    unittest.main()
