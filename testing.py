from words_to_number import words_to_number
from number_to_words import number_to_words
from all_wordifications import all_wordifications
import unittest
import time

class TestPhoneConversion(unittest.TestCase):

    def test_word2num(self):
        self.assertEqual(words_to_number('1-800-PAINTER'), '1-800-724-6837')
        self.assertEqual(words_to_number('1-800-testing'), '1-800-837-8464')
        self.assertEqual(words_to_number('1-800-426-9834'), '1-800-426-9834')
        self.assertEqual(words_to_number('1-800-DOMINOS'), '1-800-366-4667')
        self.assertEqual(words_to_number('1-800-YES-okay'), '1-800-937-6529')
        self.assertEqual(words_to_number('1-800-1O0-A12B'), '1-800-160-2122')

    def test_num2word(self):
        self.assertEqual(number_to_words('1-800-724-6837'), '1-800-PAINTER')
        self.assertEqual(number_to_words('1-800-259-2979'), '1-800-ALWAYS7')
        self.assertEqual(number_to_words('1-800-9259-297'), '1-800-9ALWAYS')
        self.assertEqual(number_to_words('1-800-882-3476'), '1-800-TUBE347')
        self.assertEqual(number_to_words('1-800-6463725'), '1-800-MINERAL')
        self.assertEqual(number_to_words('1-800-8872-4-38'), '1-800-TURBID3')

    def test_allword(self):
        # create a list of all wordifications for a phone number
        # convert all wordifications back to numbers to verify they are correct
        all_wordifications('1-800-724-6837')
        f = open("wordifications.txt", "r")
        for line in f:
            self.assertEqual(words_to_number(line[:-1]), '1-800-724-6837')
        f.close()
        all_wordifications('1-800-223-8945')
        f = open("wordifications.txt", "r")
        for line in f:
            self.assertEqual(words_to_number(line[:-1]), '1-800-223-8945')
        f.close()
        all_wordifications('1-800-6463725')
        f = open("wordifications.txt", "r")
        for line in f:
            self.assertEqual(words_to_number(line[:-1]), '1-800-646-3725')
        f.close()

if __name__ == '__main__':
    unittest.main()