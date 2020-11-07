import re
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