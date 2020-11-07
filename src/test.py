import numpy
import nltk
import spacy
import simplify_functions
import reader
from inspector_functions import *
from tkinter import *

def main_test():
    print("hi2")
    file_input = open("input.txt", "r")
    sentences = []
    for line in file_input.read().splitlines():
        sentences.extend(nltk.sent_tokenize(line))
    print(sentences)
    tokens = nltk.word_tokenize(sentences[0])
    print(tokens)
    tagged = nltk.pos_tag(tokens)
    print(tagged[0:6])
    entities = nltk.chunk.ne_chunk(tagged)
    print(entities)
    nlp = spacy.load('en')

    reader.company_name = "Apple".lower()

    for sentence in sentences:
        parsed_text = nlp(simplify_functions.simplify(sentence))
        print(nltk.pos_tag(nltk.word_tokenize(simplify_functions.simplify(sentence))))
        '''for i in parsed_text:
        print(str(i) + " " + str(i.dep_))
        print(parsed_text)'''
        subject = find_subject(parsed_text)
        if subject != None and is_synonym(subject, reader.client_synonyms):
            show_sentence(sentence, get_predicate_type(parsed_text))
        if subject != None and is_synonym(subject, reader.get_company_synonyms()):
            print("BOO!" + sentence, get_predicate_type(parsed_text))

if __name__ == "__main__":
    main_test()

# x = Tk()

# x.mainloop()
