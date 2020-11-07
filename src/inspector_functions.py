import spacy
from enum import Enum

try:
    from src.reader import *
except:
    from reader import *

class PredicateType(Enum):
    OBLIGATORY = -1
    NEUTRAL = 0
    PERMISSIVE = 1


def show_sentence(sentence, ptype):
    if ptype == PredicateType.OBLIGATORY:
        print("Warning: " + sentence)
    elif ptype == PredicateType.PERMISSIVE:
        print("Good News!: " + sentence)
    else:
        print("Boring: " + sentence)


def is_synonym(word, keywords):
    word = str(word.orth_).lower()
    return word in keywords


def is_keyword(parsed_text, index, keywords):
    word = str(parsed_text[index].orth_).lower()
    if word in keywords:
        line = keywords[word]
        for i in range(line.__len__()):
            if str(parsed_text[index + 1 + i].orth_).lower() != line[i]:
                return False
        return True
    return False


def get_predicate_type_indexed(parsed_text, index):
    if is_keyword(parsed_text, index, obligatory_verbs_constant):
        return PredicateType.OBLIGATORY
    elif is_keyword(parsed_text, index, obligatory_verbs):
        if index > 0 and check_negation(parsed_text, index - 1, -1):
            return PredicateType.PERMISSIVE
        return PredicateType.OBLIGATORY
    elif is_keyword(parsed_text, index, permissive_verbs):
        if index < parsed_text.__len__() - 1 and check_negation(parsed_text, index + 1, 0):
            return PredicateType.OBLIGATORY
        return PredicateType.PERMISSIVE
    elif index > 0:
        return get_predicate_type_indexed(parsed_text, index - 1)
    return PredicateType.NEUTRAL


def get_predicate_type(parsed_text):
    id = find_predicate_id(parsed_text)
    if id == -1:
        return PredicateType.NEUTRAL
    return get_predicate_type_indexed(parsed_text, id)


def check_negation(parsed_text, index, direction):
    if parsed_text[index].dep_ == "neg":
        return True
    elif direction != 0 and index + direction >= 0 and index + direction < parsed_text.__len__():
        return check_negation(parsed_text, index + direction, direction)
    return False


'''
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
'''


def find_type_id(parsed_text, type_name):
    for i in range(parsed_text.__len__()):
        if parsed_text[i].dep_ == type_name:
            return i
    return -1


def find_subject_id(parsed_text):
    return find_type_id(parsed_text, "nsubj")


def find_subject(parsed_text):
    id = find_subject_id(parsed_text)
    if id == -1:
        return None
    return parsed_text[id]


def find_predicate_id(parsed_text):
    return find_type_id(parsed_text, "ROOT")


def find_predicate(parsed_text):
    id = find_predicate_id(parsed_text)
    if id == -1:
        return None
    return parsed_text[id]
