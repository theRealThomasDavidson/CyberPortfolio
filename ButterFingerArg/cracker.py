"""
This is slightly modified code from https://inventwithpython.com/vigenereDictionaryHacker.py
# Vigenere Cipher Dictionary Hacker
# http://inventwithpython.com/hacking (BSD Licensed)

I basically just used this as a basic template, removed references to pyperclip as that wasn't used on my computer, moved the magic numbers data to the top of the file so that they can be modified easily and replaced the detectEnglish module with my own detect english module that is based on a language learning model to classify english and cyphertext.

This bit of code will take a list of words from the KEYWORD_FILE to decrypt a message that is in a string CIPHER_TEXT as encrypted with a vigenere cipher. when it decides that a particular decryption looks good, it will show you the key and  the decrypted message, it will ask if you think that is right or if it should continue.
"""

CIPHER_TEXT = """ilay egehyu ythb ewehyuhtbaht"""
KEYWORD_FILE = 'words.txt'

import detectEnglish2 as detect
import vigenereCipher


def main():
    ciphertext = CIPHER_TEXT
    hackedMessage = hackVigenere(ciphertext)
    if hackedMessage != None:
        print(hackedMessage)
    else:
        print('Failed to hack encryption.')

def hackVigenere(ciphertext):
    fo = open(KEYWORD_FILE)
    words = fo.readlines()
    fo.close()
    for word in words:
        word = word.strip() # remove the newline at the end
        decryptedText = vigenereCipher.decryptMessage(ciphertext, word)
        if detect.isEnglish(decryptedText, wordPercentage=50):
            # Check with user to see if the decrypted key has been found.
            print()
            print('Possible encryption break:')
            print('Key ' + str(word) + ': ' + decryptedText[:100])
            print()
            print('Enter D for done, or just press Enter to continue breaking:')
            response = input('> ')
            if response.upper().startswith('D'):
                return decryptedText
if __name__ == '__main__':
    main()