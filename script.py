### Lemmatization
#Natasha

# Pymorphy2

# spaCy
import spacy
from spacy import load
from spacy.lang.ru.examples import sentences
from spacy.lang.ru import Russian

nlp = Russian()

doc = nlp(u"Ёж диспетчер на праздник стал ужом и виноградными косточками а лаборанты ушли в отпуск звезды на небе и мишки в кино зачем мы попали под это давно ох что же мы будем делать с тобой мой мир моя слабость и ты мой герой")
# doc = nlp(u"If only you knew and be mine if I could take the stars and write your name")

for token in doc:
    print(token, token.lemma, token.lemma_)

for token in doc:
    print(token.lemma_) 

# PyMystem3

# Snowball