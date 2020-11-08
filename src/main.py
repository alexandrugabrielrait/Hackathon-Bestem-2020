import nltk
import spacy
from tkinter import *
try:
    import src.string_functions
    import src.reader
    from src.definitions import SubjectType, PredicateType
    from src.inspector_functions import *
except:
    import string_functions
    import reader
    from definitions import SubjectType, PredicateType
    from inspector_functions import *

def main():
    print("hi2")
    file_input = open("input.txt", "r", encoding='utf-8')
    sentences = []
    full_text = string_functions.utf8_to_ascii(file_input.read())
    print("def", string_functions.find_definitions(full_text))
    for line in full_text.splitlines():
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
    sets_by_subject = [set() for i in range(len(SubjectType))]
    sets_by_predicate = [set() for i in range(len(PredicateType))]

    for sentence in sentences:
        parsed_text = nlp(string_functions.simplify(sentence))
        print(nltk.pos_tag(nltk.word_tokenize(string_functions.simplify(sentence))))
        '''for i in parsed_text:
        print(str(i) + " " + str(i.dep_))
        print(parsed_text)'''
        sets_by_subject[int(get_subject_type(parsed_text).value)].add(sentence)
        sets_by_predicate[int(get_predicate_type(parsed_text).value)].add(sentence)
        """ if subject != None and is_synonym(subject, reader.client_synonyms):
            show_sentence(sentence, get_predicate_type(parsed_text))
        if subject != None and is_synonym(subject, reader.get_company_synonyms()):
            print("BOO!" + sentence, get_predicate_type(parsed_text)) """
    
    print(sets_by_subject)
    print(sets_by_predicate)

if __name__ == "__main__":
    main()
