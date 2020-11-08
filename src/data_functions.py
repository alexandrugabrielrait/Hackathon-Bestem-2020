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

def find_sets(text):
    sentences = []
    for line in text.splitlines():
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
        parsed_text = nlp(simplify(sentence))
        print(nltk.pos_tag(nltk.word_tokenize(sentence_functions.simplify(sentence))))
        '''for i in parsed_text:
        print(str(i) + " " + str(i.dep_))
        print(parsed_text)'''
        sets_by_subject[int(get_subject_type(parsed_text).value)].add(sentence)
        sets_by_predicate[int(get_predicate_type(parsed_text).value)].add(sentence)
        """ if subject != None and is_synonym(subject, reader.client_synonyms):
            show_sentence(sentence, get_predicate_type(parsed_text))
        if subject != None and is_synonym(subject, reader.get_company_synonyms()):
            print("BOO!" + sentence, get_predicate_type(parsed_text)) """

    print((sets_by_subject, sets_by_predicate))
    return (sets_by_subject, sets_by_predicate)