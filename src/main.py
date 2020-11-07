import numpy
import nltk
import spacy
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

parsed_text = nlp(sentences[1])

def find_triplet(parsed_text):
    subject = ""
    indirect_object = ""
    direct_object = ""
    for text in parsed_text:
        #subject would be
        print(str(text) + " " + str(text.dep_))
        if text.dep_ == "nsubj":
            subject = text.orth_
        #iobj for indirect object
        if text.dep_ == "iobj":
            indirect_object = text.orth_
        #dobj for direct object
        if text.dep_ == "dobj":
            direct_object = text.orth_
    return (subject, indirect_object, direct_object)

print(find_triplet(parsed_text)[0])

#x = Tk()

#x.mainloop()