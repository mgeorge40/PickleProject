# Function number_to_words() will convert a phone number into an English word
# Currently finds the longest English word that corresponds to the phone number or a subset of the phone number
# author Michelle George, mgeorge40@gatech.edu

from nltk.corpus import wordnet

dictionary = {'2':'ABC', '3':'DEF', '4':'GHI', '5':'JKL', '6':'MNO', '7':'PQRS', '8':'TUV', '9':'WXYZ'}

def number_to_words(number):
    # First check to see if we have enough numbers to make a phone number
    # Our phone number should also start with 1-800-
    # Don't accept phone numbers that already contain letters
    if number[0:6] != '1-800-' and (len(number) != 13 or len(number) != 14):
        raise Exception('The input should be a phone number starting with 1-800- followed by 7 more digits. The inputted phone number was {}'.format(number))
    groups = number.split('-')  # separate groups of numbers, removing dashes
    # FOR NOW assume number was inputted correctly with 1-800- at start
    numbers = ''.join(groups[2:]) # join all groups of numbers that were separated by dashes
    if not numbers.isdigit() or '0' in numbers or '1' in numbers:
        raise Exception('The input should be a phone number starting with 1-800- followed by 7 more integers between 2 and 9, containing no letters. The inputted phone number was {}'.format(number))
    length = len(numbers)
    # try the longest words first, then step down your length (l) if no words are found
    for l in range(length, 0, -1):
        # increment your starting position (s)
        for s in range(0, length-l+1, 1):
            word = getword(numbers[s:s+l], '', 0)
            # use getword function, if it returns None then no real English word was found at this start position and length
            if word != None:
                # if it is a word, create a phone number with it (add back the 1-800- and any unused numbers)
                phone = create_phonenumber(word, numbers, s, l)
                return phone

def getword(numbers, output, count):
    letters = dictionary[numbers[count]]
    for n in letters: # cycles through each possible letter for the corresponding number
        output = output + n # add that letter to your word
        if count+1 != len(numbers): # if we haven't reached the end of the numbers, loop again
            phone = getword(numbers, output, count+1)
            # once the lowest level recursion returns, we want to save this string which is now our phone number
            if phone != None:
                return phone
        else: # check to see if our now full string is a word
            if wordnet.synsets(output.lower()):
                phone = output
                return phone
        output = output[:-1] # remove the last letter so in the next loop we can replace it

def create_phonenumber(word, numbers, start, length):
    phone = '1-800-' + numbers[0:start] + word + numbers[start+length-1:-1]
    return phone
