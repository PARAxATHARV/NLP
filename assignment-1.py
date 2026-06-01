import re
import nltk
import spacy

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download("punkt")
nltk.download('punkt_tab')
nltk.download("stopwords")

nlp = spacy.load("en_core_web_sm")

text = """

Natural Language Processing, also known as NLP, is one of the most important areas of Artificial Intelligence.
Today, companies use NLP in chatbots, search engines, recommendation systems, social media analytics,
customer feedback analysis, automatic translation, and voice assistants.For example, a customer may write: "I LOVE this product!!!
 Visit https://example.com/product123 #Amazing #AI".Another user may write: "The service was not good... I waited 45 minutes and no one replied."
"""

text_clean = re.sub(r"http\S+|https\S+", "", text)
text_clean = re.sub(r"#[A-Za-z0-9_]+", "", text_clean)

print(text_clean)

text_lower = text_clean.lower()
print("\nAfter lowercase:")
print(text_lower)

tokens = word_tokenize(text_lower)
print("\nAfter tokenization:")
print(tokens)
stop_words = set(stopwords.words("english"))
    