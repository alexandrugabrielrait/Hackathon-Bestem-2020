import nltk
try:
    import src.sentence_functions
    import src.reader
    from src.definitions import SubjectType, PredicateType
    from src.sentence_functions import *
except:
    import sentence_functions
    import reader
    from definitions import SubjectType, PredicateType
    from sentence_functions import *

nlp = spacy.load('en')

def set_company_name(name):
    reader.company_name = name.lower()

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
                elif in_quotes:
                    current_string = current_string.__add__(c)
            if in_quotes:
                current_string = current_string.__add__(" ")
    return definitions

def find_sentences(text):
    sentences = []
    for line in text.splitlines():
        sentences.extend(nltk.sent_tokenize(line))

    return sentences

def find_sets(sentences):
    return ([{'User needs patience.', "User doesn't need patience."}, set(), {'"No sir e" mean no.'}], [{"User doesn't need patience."}, {'"No sir e" mean no.'}, {'User needs patience.'}])

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

def find_showable_list(filters, sentences):
    showable_list = []
    sets = find_sets(sentences)
    showable_set = apply_filters(filters, sets)
    for sentence in sentences:
        if sentence in showable_set and not sentence in showable_list:
            showable_list.append(sentence)
    return showable_list

