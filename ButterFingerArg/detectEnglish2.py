"""
This file is basically just a replacement of the isEnglish function in from https://inventwithpython.com/detectEnglish.py that was originally used in some code that I stole(with attribution). The additional functionality for this is basically speed, (though that could be solved with replacing a list with a set), but that function required known english words separated by spaces, but this just requires something to be "englishy", so english words not separated by spaces or things like 'chloroethanthiol' that might be reasonably absent from any dictionary but a word that makes perfect sense in English.
The pickle file is a sklearn object that was trained in ml_learner.py.
"""

import pickle
from time import time

start= time()
print(f"starting loading pickle.")
with open("trained_.pkl", "rb") as cucumber:
    model = pickle.load(cucumber)
print(type(model))
print(f"loaded pickle in {time()-start}s")

def isEnglish(decryptedText:str, wordPercentage=None):
    return (model.predict((decryptedText, )) == "eng")[0]

def main():
    start= time()
    print(f"starting classifying")
    print(isEnglish("kasjl asas amr wehsajas saas"))
    print(isEnglish("where is my supersuit geh"))
    print(isEnglish("chloroethanthiol"))
    print(f"classified 2 in {time()-start}s")

if __name__ == "__main__":
    main()