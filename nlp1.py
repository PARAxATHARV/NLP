import nltk
import re 

from nltk.corpus import stopwords 
from nltk.tokenize import wordpunct_tokenize

nltk.download("stopwords")
nltk.download("punk_tab")

text = "the sky is clear and the stars are twinkling in the night ."
tokens = wordpunct_tokenize(text)

stop_words = set(stopwords.words("english"))

filtered_words = [
    word for word in tokens 
    if word.lower() not in stop_words
]
print(filtered_words)