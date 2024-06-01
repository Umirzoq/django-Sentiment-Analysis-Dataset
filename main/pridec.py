import random
import re
import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer as tf


def clean(text):
    text = re.sub(r'[^a-zA-Z\s]', '', str(text))
    text = text.lower()
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def execute2(txt):
    return random.choice([1, 2, 3])


def execute(txt):
    df = pd.read_csv('main/training.csv',
                     delimiter=',', encoding='ISO-8859-1')
    df.columns = ['sentiment', 'id', 'date', 'query', 'user', 'text']
    df = df.drop_duplicates('text')
    df['text'] = df['text'].apply(clean)
    vectorizer = tf()
    x = df['text']
    vectorizer.fit_transform(x)
    models = pickle.load(open("main/data.pickle", 'rb'))
    new_text_vector = vectorizer.transform([txt])
    prediction = models.predict(new_text_vector)
    print(prediction[0])
    return prediction[0]
