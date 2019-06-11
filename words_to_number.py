# Function words_to_number() will convert a phone number with a word in it to only numbers
# author Michelle George, mgeorge40@gatech.edu

dictionary = {'A':'2', 'B':'2', 'C':'2', 'D':'3', 'E':'3', 'F':'3', 'G':'4', 'H':'4', 'I':'4', 'J':'5',
               'K':'5', 'L':'5', 'M':'6', 'N':'6', 'O':'6', 'P':'7', 'Q':'7', 'R':'7', 'S':'7', 'T':'8',
               'U':'8', 'V':'8', 'W':'9', 'X':'9', 'Y':'9', 'Z':'9'}

def words_to_number(str):
    groups = str.split('-') # separate groups of numbers, removing dashes
    # FOR NOW assume number was inputted correctly with 1-800- at start
    output = '1-800-'
    count = 0 # use this count to know where to put the - back in
    for group in groups[2:]:
        for i in group:
            if i.isdigit():
                output = output + i
            else:
                output = output + dictionary[i.capitalize()]
            if count == 2:
                output = output + '-'
            count += 1
    return(output)