import re
import string
import spacy

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# 1. Create dataset: 10 movie descriptions
movies = [
    {
        "title": "Galaxy Quest",
        "description": "A team of astronauts travel through space and meet friendly robots."
    },
    {
        "title": "Robot Planet",
        "description": "A young engineer discovers a planet full of intelligent robots."
    },
    {
        "title": "Space Adventure",
        "description": "Explorers go on a dangerous adventure across distant galaxies."
    },
    {
        "title": "Healthy Life",
        "description": "A documentary about healthy food, exercise, and good lifestyle habits."
    },
    {
        "title": "The Football Dream",
        "description": "A young player trains hard to become a famous football star."
    },
    {
        "title": "Cooking Master",
        "description": "A chef teaches simple recipes using fresh vegetables and healthy ingredients."
    },
    {
        "title": "Mystery House",
        "description": "A detective investigates strange events inside an old house."
    },
    {
        "title": "Ocean Journey",
        "description": "A group of friends travel across the ocean and discover hidden islands."
    },
    {
        "title": "Future AI",
        "description": "Scientists create artificial intelligence systems that help humans."
    },
    {
        "title": "Lost in Space",
        "description": "A family gets lost in space and depends on a robot to survive."
    }
]

