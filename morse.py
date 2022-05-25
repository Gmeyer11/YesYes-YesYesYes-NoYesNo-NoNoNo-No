# Python program to implement Morse Code Translator
 
'''
VARIABLE KEY
'cipher' -> 'stores the morse translated form of the english string'
'decipher' -> 'stores the english translated form of the morse string'
'citext' -> 'stores morse code of a single character'
'i' -> 'keeps count of the spaces between morse characters'
'message' -> 'stores the string to be encoded or decoded'
'''
 
# Dictionary representing the morse code chart
MORSE_CODE_DICT = { 'A':'NoYes', 'B':'YesNoNoNo',
                    'C':'YesNoYesNo', 'D':'YesNoNo', 'E':'No',
                    'F':'NoNoYesNo', 'G':'YesYesNo', 'H':'NoNoNoNo',
                    'I':'NoNo', 'J':'NoYesYesYes', 'K':'YesNoYes',
                    'L':'NoYesNoNo', 'M':'YesYes', 'N':'YesNo',
                    'O':'YesYesYes', 'P':'NoYesYesNo', 'Q':'YesYesNoYes',
                    'R':'NoYesNo', 'S':'NoNoNo', 'T':'Yes',
                    'U':'NoNoYes', 'V':'NoNoNoYes', 'W':'NoYesYes',
                    'X':'YesNoNoYes', 'Y':'YesNoYesYes', 'Z':'YesYesNoNo',
                    '1':'NoYesYesYesYes', '2':'NoNoYesYesYes', '3':'NoNoNoYesYes',
                    '4':'NoNoNoNoYes', '5':'NoNoNoNoNo', '6':'YesNoNoNoNo',
                    '7':'YesYesNoNoNo', '8':'YesYesYesNoNo', '9':'YesYesYesYesNo',
                    '0':'YesYesYesYesYes', ', ':'YesYesNoNoYesYes', 'No':'NoYesNoYesNoYes',
                    '?':'NoNoYesYesNoNo', '/':'YesNoNoYesNo', '.':'YesNoNoNoNoYes',
                    '(':'YesNoYesYesNo', ')':'YesNoYesYesNoYes'}
 
# Function to encrypt the string
# according to the morse code chart
def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':
 
            # Looks up the dictionary and adds the
            # corresponding morse code
            # along with a space to separate
            # morse codes for different characters
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            # 1 space indicates different characters
            # and 2 indicates different words
            cipher += ' '
 
    return cipher
 
# Function to decrypt the string
# from morse to english
def decrypt(message):
 
    # extra space added at the end to access the
    # last morse code
    message += ' '
 
    decipher = ''
    citext = ''
    for letter in message:
 
        # checks for space
        if (letter != ' '):
 
            # counter to keep track of space
            i = 0
 
            # storing morse code of a single character
            citext += letter
 
        # in case of space
        else:
            # if i = 1 that indicates a new character
            i += 1
 
            # if i = 2 that indicates a new word
            if i == 2 :
 
                 # adding space to separate words
                decipher += ' '
            else:
 
                # accessing the keys using their values (reverse of encryption)
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
                .values()).index(citext)]
                citext = ''
 
    return decipher
 
# Hard-coded driver function to run the program
def main():
    message = "morse"
    result = encrypt(message.upper())
    print (result)
 
    message = "NoNoNoNo No NoYesNoNo NoYesNoNo YesYesYes NoNoYesYesNoNo  NoNo NoNoNo  Yes NoNoNoNo NoNo NoNoNo  Yes NoNoNoNo NoNo YesNo YesYesNo  YesYesYes YesNo NoNoYesYesNoNo"
    result = decrypt(message)
    print (result)
 
# Executes the main function
if __name__ == '__main__':
    main()
