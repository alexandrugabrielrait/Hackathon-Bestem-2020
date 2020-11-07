import re
try:
    from src.reader import replacements
except:
    from reader import replacements

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

transl_table = dict( [ (ord(x), ord(y)) for x,y in zip( u"‘’´“”–-",  u"'''\"\"--") ] )

def utf8_to_ascii(string):
    return string.translate(transl_table)

def cp1252_to_ascii(string):
    return utf8_to_ascii(string.encode('cp1252').decode("utf-8"))

def find_definitions(string):
    definitions = []
    current_string = ""
    in_quotes = False
    for l in string.splitlines():
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