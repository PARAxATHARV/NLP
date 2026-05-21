import spacy

nlp = spacy.load("en_core_web_sm")
text = "researchers analayze large datasets efficently."

doc = nlp(text)

for token in doc:
    print(
        f"{token.text:<15}"
        f"{token.text:<15}"
        f"{token.head.text}"
    )
