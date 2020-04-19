import pickle
import bs4
import re
from urllib.request import urlopen
import os
basepath = os.path.abspath(".")

with open('model.model', 'rb') as f:
     model = pickle.load(f)

with open('model.vec', 'rb') as f:
     vectorizer = pickle.load(f)
print(model)
print(vectorizer)

def get_text_by_url(url):
    html=urlopen(url)
    soup = bs4.BeautifulSoup(html, 'html.parser')
    soup = re.sub(r'\s+', ' ', soup.get_text())
    return soup



def get_data(text):
    return vectorizer.transform([text])


def predict(url):
    print(url)
    text=get_text_by_url(url)
    data=get_data(text)
    return model.predict_proba(data)
