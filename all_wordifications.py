# Function all_wordifications() will output a text file with a list of all possible phone numbers
# These phone numbers include an English word and any unused numbers
# author Michelle George, mgeorge40@gatech.edu

from nltk.corpus import words

dictionary = {'2':'ABC', '3':'DEF', '4':'GHI', '5':'JKL', '6':'MNO', '7':'PQRS', '8':'TUV', '9':'WXYZ'}

def all_wordifications(number):
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
    # Create an output file to store all your word/number combinations in
    f = open("wordifications.txt", "w+")
    length = len(numbers)
    # try the longest words first, then step down your length (l) if no words are found
    for l in range(length, 0, -1):
        # increment your starting position (s)
        for s in range(0, length-l+1, 1):
            phone_list = []
            wordlist = getwordlist(numbers[s:s+l], '', 0, [])
            # use getwordlist function, will return a list of all possible words at this start position and length
            if wordlist != None:
                for word in wordlist:
                    # for each word, create a phone number with it and add it to the file
                    phone = create_phonenumber(word, numbers, s, l)
                    f.write(phone + '\n')
    f.close()
    return

def getwordlist(numbers, output, count, phone_list):
    letters = dictionary[numbers[count]]
    for n in letters: # cycles through each possible letter for the corresponding number
        output = output + n # add that letter to your word
        if count+1 != len(numbers): # if we haven't reached the end of the numbers, loop again
            phone = getwordlist(numbers, output, count+1, phone_list)
        else: # check to see if our now full string is a word
            if output.lower() in words.words():
                phone = output
                phone_list.append(phone) # if it is a word, add it to our output list
        output = output[:-1] # remove the last letter so in the next loop we can replace it
    return phone_list

def create_phonenumber(word, numbers, start, length):
    phone = '1-800-' + numbers[0:start] + word + numbers[start+length:]
    return phone