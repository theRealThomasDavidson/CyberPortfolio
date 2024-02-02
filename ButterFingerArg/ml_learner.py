"""
This trains a model to classify languages based on a sample of the language. in this case we are just training to choose between ciphertext of english put through a vigenere cipher "cyf" and english phrases "eng". It then takes this trained model and writes it to IN_FILE as a picklefile. The labeled data is found initially in INFILE. 
"""

OUT_FILE = "trained_.pkl"
IN_FILE = "labeled_data.csv"


import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn import svm
from pickle import dump

# set up Training
df = pd.read_csv(IN_FILE, encoding = "ISO-8859-1")
samples = df['sample']
labels = df['label']

vec_opts = {
    "ngram_range": (1, 8),
    "analyzer": "word",
    "token_pattern": "..",
    "min_df": 3,
}
vec = CountVectorizer(**vec_opts)
model = vec.fit_transform(labels, samples)

# term frequency–inverse document frequency we add addtional weight to words that don't appear a lot (so the noops that are 0**32 in all arches don't count for much you see)
idf_opts = {"use_idf": True}
idf = TfidfTransformer(**idf_opts)

clf_opts = {"kernel": "linear"}
clf = svm.SVC(**clf_opts)

# Perform the idf transform
model = idf.fit_transform(model)

# Created pipeline for ease of testing
pipeline = Pipeline([
    ('vec',  CountVectorizer(**vec_opts)),
    ('idf',  TfidfTransformer(**idf_opts)),
    ('clf',  svm.SVC(**clf_opts))
])

# Training my algorithm
model = pipeline.fit(labels, samples)

if __name__ == "__main__":
    dump(model, open(OUT_FILE,'wb'))
