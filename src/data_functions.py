import nltk
import spacy
try:
    import src.reader
    from src.definitions import SubjectType, PredicateType
    from src.sentence_functions import *
except:
    import reader
    from definitions import SubjectType, PredicateType
    from sentence_functions import *

nlp = spacy.load('en')

'''
    Sets the company name that can be used as a synonym for company
'''
def set_company_name(name):
    reader.company_name = name.lower()

'''
    Finds definitions in the text. Definitions are tagged by quotes
'''
def find_definitions(text):
    definitions = []
    current_string = ""
    in_quotes = False
    for l in text.splitlines():
        for s in l.split():
            for c in s:
                if c == '"':
                    in_quotes = not in_quotes
                    if not in_quotes and current_string != "" and current_string not in definitions:
                        definitions.append(current_string)
                        current_string = ""
                elif in_quotes:
                    current_string = current_string.__add__(c)
            if in_quotes:
                current_string = current_string.__add__(" ")
    return definitions

'''
    Returns the list of sentences from a text
'''
def find_sentences(text):
    sentences = []
    for line in text.splitlines():
        sentences.extend(nltk.sent_tokenize(line))
    return sentences

'''
    Returns a tuple of sets with sentences, grouped by subject and predicate types
'''
def find_sets(sentences):
    sets_by_subject = [set() for i in range(len(SubjectType))]
    sets_by_predicate = [set() for i in range(len(PredicateType))]
    
    for sentence in sentences:
        parsed_text = nlp(sentence)
        sets_by_subject[int(get_subject_type(parsed_text).value)].add(sentence)
        sets_by_predicate[int(get_predicate_type(parsed_text).value)].add(sentence)
    return (sets_by_subject, sets_by_predicate)

'''
    Returns a set of sentences from the sets that match the filters
'''
def apply_filters(filters, sets):
    subject_set = set()
    predicate_set = set()
    for i in range(len(SubjectType)):
        if filters[i]:
            subject_set.update(sets[0][i])
    for i in range(len(PredicateType)):
        if filters[len(SubjectType) + i]:
            predicate_set.update(sets[1][i])
    return subject_set.intersection(predicate_set)

'''
    Returns a list of sentences that match the filters
'''
def find_showable_list(filters, sentences):
    showable_list = []
    sets = find_sets(sentences)
    showable_set = apply_filters(filters, sets)
    for sentence in sentences:
        if sentence in showable_set and not sentence in showable_list:
            showable_list.append(sentence)
    return showable_list

