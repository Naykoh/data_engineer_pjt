"""
    process_and_predict.py
    ----------------

    This package contains function to process a sentence and predict if it is positive or negative sentiment
"""

import pickle
from pathlib import Path
import numpy as np


ROOT = Path(__file__).resolve().parents[2]

from tensorflow import keras

model = keras.models.load_model(ROOT/'models')


# Getting back the objects:
with open(ROOT/'models/objs.pkl','rb') as f:  # Python 3: open(..., 'rb')
    tokenizer,pad_sequences, max_length = pickle.load(f)

def classifier(text):
    review_seq = tokenizer.texts_to_sequences([text])
    review_padded = pad_sequences(review_seq,maxlen = max_length, padding = 'post')
    prediction = model.predict(review_padded)
    max_classifier = np.argmax(prediction)
    if max_classifier == 0:
        return "neutral"
    elif max_classifier == 1:
        return "positive"
    elif max_classifier == 2:
        return "negative"


def predict(sentence):
    """
        predict if a sentence has a positive or negative sentiment

        :param processed_sentence: sentence to predict
    """
    classing = classifier(sentence)
    return classing
