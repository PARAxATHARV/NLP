import spacy 

nlp = spacy.load("en_core_web_sm")

text = "the sky is clear and stars are twinkling ."

doc = nlp(text)
words =[
    "delayed"
    "travelling"
    
]
for words in words:
    print("real world: ",words)
    print("spacy:",nlp(words))