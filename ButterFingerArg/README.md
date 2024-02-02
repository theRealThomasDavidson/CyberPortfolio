# The Butterfinger/Wisecrack ARG that wasn't

This is a self motivated exercise in cryptographic cracking. Done in a limited amount of time approximately approximately 1 business day at odd times. 

### Setting the Scene

On a long drive I was listening to a live podcast on youtube. This podcast was produced by a channel called Wisecrack, and a long term sponsor Butterfinger candy. During the episode they hinted at a cryptographic game to be played in about 2 days, and gave some hints

time=2m38s
Burns: [Maybe, there's a secret cipher with the secret code in the video on Wednesday. I don't know!](https://www.youtube.com/watch?v=CGcTCvxKd6U&t=158s) 

time=46m33s
Burns: [First, you can play by figuring out the code there's a cipher guys there's a cipher Lux(the other host) made a cipher. I've learned about ciphers as part of this process. Vigenere, things of that nature. Yes!](https://www.youtube.com/watch?v=CGcTCvxKd6U&t=2793s)

So, I think sure let's get a Vigenere decrypter and get that prize. we've got a day to get this all together so once I get my stuff together on Monday evening I'll have a few hours in the morning on Tuesday as well as a any time before bed that I can muster.

### What is a Vigenere Cipher?

So, I didn't know how these kinds of ciphers worked off the bat, I looked it up on wikipedia and found that basically each letter in the message gets a caesar cipher applied based on the keyword. The letters of the keyword would be repeated in order until the message was over for example if the keyword was red and the message was 16 characters long you would have a key of "redredredredredr". And each letter of this key would show the offset of the caesar cipher for the character in it's index, with an a->0, b->1 c->2 ... z->25. so to decrypt this we basically use the same cipher but with negative offsets, just like a caesar cipher.

### Blatent Theft

So, I immediately thought to look for previous implementations of this in python. I found inventwithpython.com which talks a bit about both doing encryption/decryption and cracking. I ended up using both of those basically unchanged and they can be found at ./cracker.py for the cracking, and ./vigerereCipher.py for the encryption/decryption. But I noticed a few things with the ./detectEnglish.py file that I found concerning, basically it required the message to display known words from a dictionary file, while this is not the biggest issue overall as it could have some of the words missing and still flag a partial match, it required all the words to be separated by spaces which I was not fully convinced would be the case for the ciphertext that was to be released.

### Gathering Keywords and Phrases

At this point I was fairly confident that I could solve a cipher If given a list of possible keywords and either a particular setup on the message and how it's displayed. So, I'll first solve the problem of finding keywords, first I used a web crawler(./web_crawler.py) to check for view the tree of a single website and look for any text information. I was initially hoping to do this with gamewithbutterfinger.com but I was immediately asked to do a post request on the first page to see any additional information or links and with limited time I decided instead ot use butterfinger.com. I collected any of the text elements as whole phrases to store into a file to use later. Next, I went back to previous podcasts for this series on youtube, I got the video tag of those videos in my browser and used the python library youtube_transcript_api to get the closed captioning for them. I took each of the closed captions that are displayed together and made them their own phrase file.

So, now with these phrase files I was able to grab any words that were used and any two word phrases that were repeated this was done with the ./strip_list.py code. And now we have english phrases and a list of possible keywords for the puzzle.

### What is English Anyway?

So, we still haven't found out how to work around the limitations of the detectEnglish module yet, but it's 2024, so lets use that 2024est of all technologies to help me out. Language Learning Models! So, I asked ChatGPT if there were any technologies that could tell me if a bit of text was english or ciphertext, it suggested using a Language Learning Model. I wish I thought of that. Well, I had a machine code classifier to determine if some binary data was machine code for a program in various architectures, and I decided to reconfigure that to classify english and ciphertext. So, basically I was able to tune it for this by changing the n-gram from up to 4 bytes(most architectures' word length for that puzzle) to up to 8 characters and make it not have to convert from b64 to bytes but instead take the input as is.

Let's make some sample data! so basically I used the youtube captions as my english phrases and, to make sure that spaces or other details did not impact if how the model viewed ciphertext, I used those same english phrases encrypted with the identified keywords as the examples of ciphertext.

This data labeling was done with ./phrases2labeled.py. and the following training was done with ./ml_learner.py which output a pickle file of the trained dataset of the type sklearn.pipeline.Pipeline. This pickle file is then loaded in ./detectEnglish2.py as our english checker replacement, and the classifier is used to check if a string seems like english or not.

### Putting it all together

So now I modified the ./cracker.py file so that it incorporated ./detectEnglish2 and I pointed to the keywords files that I curated, I also grabbed a long word list incase that failed it wasn't RockYou.txt because it was supposed to be english words, but it was pretty extensive, containing a lot of lines that I wouldn't consider words. This was completed on Tuesday evening so now to wait for the video to come out.

### BETRAYAL

So, when they day rolls around, the video comes out and it has the key with the cipher. [link](https://www.youtube.com/watch?v=q7DDlZ-F5M4&t=1058s)

Oh well sometimes the work is it's own reward maybe I can do a write up on this anyway to show others how one might tackle one of these problems. 

