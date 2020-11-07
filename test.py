import numpy
import nltk
import spacy
from inspector_functions import *
from tkinter import *

file_input = open("input.txt", "r")
sentences = []
for line in file_input.readlines():
    sentences.extend(nltk.sent_tokenize(line))
print(sentences)
tokens = nltk.word_tokenize(sentences[0])
print(tokens)
tagged = nltk.pos_tag(tokens)
print(tagged[0:6])
entities = nltk.chunk.ne_chunk(tagged)
print(entities)
nlp = spacy.load('en')

for sentence in sentences:
    parsed_text = nlp(sentence)
    '''for i in parsed_text:
        print(str(i) + " " + str(i.dep_))
    print(parsed_text)'''
    if is_synonym(find_subject(parsed_text), client_synonyms):
        ptype = get_predicate_type(parsed_text)
        if ptype == PredicateType.OBLIGATORY:
            print("Warning: " + sentence)
        elif ptype == PredicateType.PERMISSIVE:
            print("Good News!: " + sentence)
        else:
            print("Boring: " + sentence)

#x = Tk()

#x.mainloop()