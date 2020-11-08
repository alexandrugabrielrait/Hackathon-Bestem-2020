import re
import spacy
try:
    from src.reader import *
except:
    from reader import *

"""
    Simplifies the input sentences by merging compound words and names.
"""
def simplify(sentence):
    for r in replacements:
        sentence = re.sub(r[0], r[1], sentence, re.IGNORECASE)
    words = sentence.split()
    new_words = list()
    n = words.__len__()
    i = 0
    while i < n:
        new_words.append(words[i])
        if i != 0 and words[i][0].isupper() and not words[i].isupper():
            for j in range(i + 1, n - 1):
                if words[j][0].isupper() and not words[j].isupper():
                    new_words[-1] += words[j]
                    found = True
                else:
                    found = False
                    break
            if found:
                i = j
        i += 1
    sentence = ' '.join(word for word in new_words)
    print(sentence)
    return sentence

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

def get_subject_type(parsed_text):
    subject = find_subject(parsed_text)
    if is_synonym(subject, client_synonyms):
        return SubjectType.CLIENT
    if is_synonym(subject, get_company_synonyms()):
        return SubjectType.COMPANY
    return SubjectType.REST

def find_predicate_id(parsed_text):
    return find_type_id(parsed_text, "ROOT")

def find_predicate(parsed_text):
    id = find_predicate_id(parsed_text)
    if id == -1:
        return None
    return parsed_text[id]

def is_keyword(parsed_text, index, keywords):
    word = str(parsed_text[index].orth_).lower()
    if word in keywords:
        line = keywords[word]
        for i in range(line.__len__()):
            if str(parsed_text[index + 1 + i].orth_).lower() != line[i]:
                return False
        return True
    return False

def check_negation(parsed_text, index, direction):
    if parsed_text[index].dep_ == "neg":
        return True
    elif direction != 0 and index + direction >= 0 and index + direction < parsed_text.__len__():
        return check_negation(parsed_text, index + direction, direction)
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