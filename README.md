# PickleProject
Translate telephone numbers between letters and numbers using standard keypad layout

Function words_to_number accepts as an input a US 1-800- phone number string containing words 
and outputs this phone number's numeric equivalent

Function number_to_words accepts as an argument a string containing an all-numeric 1-800- phone number 
and outputs an equivalent 1-800- phone number containing the longest English word possible
0s and 1s not accepted in the input because those numbers don't correspond to letters on a standard keypad

Function all_wordifications accepts as an argument a string containing an all-numeric 1-800- phone number 
and creates a file "wordifications.txt" in the same folder containing a list of all possible English
words and number combinations (words with a minimum of two letters, according to the dictionary used)
0s and 1s not accepted in the input because those numbers don't correspond to letters on a standard keypad

Conversion made using standard telephone letter layout
2 = ABC, 3 = DEF, 4 = GHI, 5 = JKL, 6 = MNO, 7 = PQRS, 8 = TUV, 9 = WXYZ

English dictionary used comes from Natural Language Toolkit (nltk)
nltk can be installed with "pip install nltk"
Ensure nltk data is downloaded by running "import nltk" and then "nltk.download(‘popular’)" in the Python interpreter