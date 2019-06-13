from words_to_number import words_to_number
from number_to_words import number_to_words
import unittest

class TestPhoneConversion(unittest.TestCase):

    def test_word2num(self):
        self.assertEqual(words_to_number('1-800-PAINTER'), '1-800-724-6837')
        self.assertEqual(words_to_number('1-800-aa-aba-00'), '1-800-222-2200')
        self.assertEqual(words_to_number('1-800-426-9834'), '1-800-426-9834')
        self.assertEqual(words_to_number('1-800-DOMINOS'), '1-800-366-4667')

    def test_num2word(self):
        self.assertEqual(number_to_words('1-800-43556'), '1-800-HELLO')
        self.assertEqual(number_to_words('1-800-228'), '1-800-ACT')
        self.assertEqual(number_to_words('1-800-724-6837'), '1-800-PAINTER')
        self.assertEqual(number_to_words('1-800-8728'), '1-800-TSA2')
        self.assertEqual(number_to_words('1-800-433-73'), '1-800-GEESE')
        self.assertEqual(number_to_words('1-800-259-2979'), '1-800-ALWAYS7')
        self.assertEqual(number_to_words('1-800-9259-297'), '1-800-9ALWAYS')


if __name__ == '__main__':
   #unittest.main()
   number_to_words('1-800-422-8764')