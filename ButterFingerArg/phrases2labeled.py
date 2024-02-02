"""
This code should generate labeled data for english phrases in IN_FILE stored one on each line and ciphertext of those same phrases into OUT_FILE as a .csv with each being labeled as either "eng" to denote english or "cyf" to denote ciphertext.
"""

IN_FILE = "human_phrases.txt"
OUT_FILE = "labeled_data.csv"
KEYWORD_FILE = "keywords.txt"

from string import punctuation
import re
from random import choice, choices, shuffle
from vigenereCipher import encryptMessage
from csv import writer

phrases = {"eng":[], "cyf":[], }
with open(IN_FILE, "r") as in_file:
    for line in in_file.readlines():
        line = line.translate(str.maketrans('', '', punctuation)).strip()
        if bool(re.search(r'\d', line)):
            continue # I don't know how to curate these with numbers so i'm gonna remove them.
        phrases["eng"].append(line)

with open(KEYWORD_FILE, "r") as in_file:
    keywords = in_file.read().split("\n")

for _ in range(len(phrases["eng"]) * 3):
    phrase = choice(phrases["eng"])
    key = False
    while not key:
        key = choice(keywords)
    phrases["cyf"].append(encryptMessage(phrase, key))

shuffle(phrases["cyf"])
shuffle(phrases["eng"])
print(phrases["cyf"][:10])
with open(OUT_FILE, "w+", newline="") as out_file:
    csv_writer = writer(out_file, delimiter=',')
    csv_writer.writerow(["label", "sample"])
    while phrases["cyf"] and phrases["eng"]:
        label = choices(("cyf", "eng"), weights = [len(phrases["cyf"]), len(phrases["eng"])])[0]
        sample = phrases[label].pop()
        csv_writer.writerow([label, sample])
