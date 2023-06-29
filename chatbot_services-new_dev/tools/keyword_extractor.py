import nltk
import sys
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def keyword_extractor(sentence):
    # Tokenize the sentence into words
    words = word_tokenize(sentence)
    # Perform Part-of-Speech (POS) tagging on the sentence
    tagged_words = nltk.pos_tag(words)
    keywords_to_exclude = {"is", "was", "am", "are","What","How","Why","does","did"}

    pos_tags = ['NN', 'NNS', 'VBD', 'VBN', 'VBP', 'VBZ', 'JJ', 'JJR', 'JJS', 'CD']
    keywords = [word for word, pos in tagged_words if pos.startswith(tuple(pos_tags)) and word not in keywords_to_exclude ]

    return keywords