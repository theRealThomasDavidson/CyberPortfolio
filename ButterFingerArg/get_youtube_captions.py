"""
This is a small function that collects phrases from a group of youtube videos and writes them to a new file as a collection of phrases seperated by lines that show up in the youtube transcript. I used this to get both a set of data to use to train a language learning model to recognise english vs ciphertext and to seed a dictionary with possible keywords. 
"""
VIDEO_TAGS = ("uTp-gqKjeKE", "CGcTCvxKd6U", "Q5uhV68tIrM", "X1iBGf2qzg4")
OUT_FILE = "./random.txt"


from youtube_transcript_api import YouTubeTranscriptApi
from unicodedata import normalize
# assigning srt variable with the list
# of dictionaries obtained by the get_transcript() function
phrases = []
for video_tag in VIDEO_TAGS:
    srt = YouTubeTranscriptApi.get_transcript(video_tag)
    phrases.extend([f"{x['start']}: {x['text'].lower()}"  for x in srt])

with open(OUT_FILE, "w+") as out_file:
    for phrase in phrases:
        phrase = normalize('NFKD', phrase).encode('ascii','ignore').decode()
        out_file.write(phrase + "\n")