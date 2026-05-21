import nltk
import re 

from nltk.stem import SnowballStemmer
from nltk.stem import LancasterStemmer

#create a stemmer object 
porter = nltk.PorterStemmer()
snowball = SnowballStemmer("english")
lancaster = LancasterStemmer()

#'list of words'
words =[
    "running"
    "studies"
    "riding"
    "happily"
    "university"
    "happiness"
]

    print(porter.stem.words)
