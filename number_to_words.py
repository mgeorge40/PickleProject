# Function number_to_words() will convert a phone number into an English word
# Currently finds an English word that corresponds to the phone number, but only the length of the number (i.e. longest word possible)
# author Michelle George, mgeorge40@gatech.edu

from nltk.corpus import wordnet

dictionary = {'2':'ABC', '3':'DEF', '4':'GHI', '5':'JKL', '6':'MNO', '7':'PQRS', '8':'TUV', '9':'WXYZ'}

def number_to_words(number):
    groups = number.split('-')  # separate groups of numbers, removing dashes
    # FOR NOW assume number was inputted correctly with 1-800- at start
    numbers = ''.join(groups[2:]) # join all groups of numbers that were separated by dashes
    output = ''
    count = 0
    phone = getword(numbers, output, count)
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
                phone = create_phonenumber(output) # if it is a word, create a phone number with it
                return phone
        output = output[:-1] # remove the last letter so in the next loop we can replace it

def create_phonenumber(word):
    # function will be expanded when shorter word capabilities are added (i.e. word and number combinations)
    phone = '1-800-' + word
    return phone
