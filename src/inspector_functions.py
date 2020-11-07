import spacy
from enum import Enum

from src.reader import *


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


def is_keyword(sentence, index, keywords):
    if sentence[index].orth_ in keywords:
        line = keywords[sentence[index].orth_]
        for i in range(line.__len__()):
            if sentence[index + 1 + i].orth_ != line[i]:
                return False
        return True
    return False


def get_predicate_type_indexed(sentence, index):
    if is_keyword(sentence, index, obligatory_verbs_constant):
        return PredicateType.OBLIGATORY
    elif is_keyword(sentence, index, obligatory_verbs):
        if index > 0 and check_negation(sentence, index - 1, -1):
            return PredicateType.PERMISSIVE
        return PredicateType.OBLIGATORY
    elif is_keyword(sentence, index, permissive_verbs):
        if index < sentence.__len__() - 1 and check_negation(sentence, index + 1, 0):
            return PredicateType.OBLIGATORY
        return PredicateType.PERMISSIVE
    elif index > 0:
        return get_predicate_type_indexed(sentence, index - 1)
    return PredicateType.NEUTRAL


def get_predicate_type(sentence):
    return get_predicate_type_indexed(sentence, find_predicate_id(sentence))


def check_negation(sentence, index, direction):
    if sentence[index].dep_ == "neg":
        return True
    elif direction != 0 and index + direction >= 0 and index + direction < sentence.__len__():
        return check_negation(sentence, index + direction, direction)
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


def find_subject_id(parsed_text):
    return find_type_id(parsed_text, "nsubj")


def find_subject(parsed_text):
    return parsed_text[find_subject_id(parsed_text)]


def find_predicate_id(parsed_text):
    return find_type_id(parsed_text, "ROOT")


def find_predicate(parsed_text):
    return parsed_text[find_predicate_id(parsed_text)]
