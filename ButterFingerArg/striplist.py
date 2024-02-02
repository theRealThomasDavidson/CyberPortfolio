"""
This file is meant to take an IN_FILE that is full of lines of multiple words and input into an OUT_FILE the individual words, or 2 wor phrases that were repeated. This was used to generate files to inform keywords in  
"""

IN_FILE = "./human_phrases.txt"
OUT_FILE = "./human_words.txt"

import string
import re

words_set = set()
words_dict = {}
with open(IN_FILE, "r") as in_file:
    for line in in_file.readlines():
        line = line.translate(str.maketrans('', '', string.punctuation))
        line = line.strip().split(" ")
        for ndx, word in enumerate(line):
            if bool(re.search(r'\d', word)):
                continue
            if not word.isalpha() and len(word) > 3:
                continue
            words_set.add(word.lower())
            if ndx == 0 or not line[ndx-1].isalpha():
                continue
            if bool(re.search(r'\d', line[ndx-1])):
                continue
            compound = (line[ndx-1] + word).lower()
            if len(compound) < 5:
                continue
            if compound not in words_dict:
                words_dict[compound] = 0
            words_dict[compound] += 1

with open(OUT_FILE, "w+") as out_file:
    for word in words_set:
        if len(word) < 3:
            continue
        out_file.write(word+"\n")
    count = 0
    for word, reps in words_dict.items():
        if reps > 2:
            if len(word) < 5:
                continue
            out_file.write(word+"\n")
            count += 1
