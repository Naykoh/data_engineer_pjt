"""
    process_and_predict.py
    ----------------

    This package contains function to process a sentence and predict if it is positive or negative sentiment
"""

import pickle
from collections import defaultdict

import pandas as pd
from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.corpus import wordnet as wn
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]



with open(ROOT/'models/modelvectorizer.pickle', 'rb') as data:
    modelvectorizer = pickle.load(data)

with open(ROOT/'models/modelclassifier.pickle', 'rb') as data:
    classifier = pickle.load(data)


def process(sentence):
    """
        apply modification to sentence to make it predictable by the ml model

        :param sentence: sentence to process

        :return: processed sentence
    """
    # remove blank rows, lower case and perform tokenization
    sentence_tokenized = word_tokenize(sentence.lower())
    
    # defaultdict is a dictionary that provides a default value if the index is not found
    # in this example, the dictionary defaults to nouns
    tag_map = defaultdict(lambda : wn.NOUN)
    tag_map['J'] = wn.ADJ
    tag_map['V'] = wn.VERB
    tag_map['R'] = wn.ADV

    stopWords = stopwords.words('english')

    word_Lemmatized = WordNetLemmatizer()

    final_words = []
    for word, tag in pos_tag(sentence_tokenized):
        # Below condition is to check for Stop words and consider only alphabets
        if word not in stopWords and word.isalpha():
            final_words.append(word_Lemmatized.lemmatize(word,tag_map[tag[0]]))
    # The final processed set of words for each iteration will be stored in 'text_final'

    return str(final_words)

def predict(processed_sentence):
    """
        predict if a sentence has a positive or negative sentiment

        :param processed_sentence: sentence to predict
    """

    
    vectorized_sentence = modelvectorizer.transform([processed_sentence])
    prediction = classifier.predict(vectorized_sentence)[0]
    return prediction


# def main():
#     pass


# if __name__ == "__main__":
#     main()
