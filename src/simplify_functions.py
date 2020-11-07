import re


"""
    Reads the replacement keywords from a file
"""
def replacement_reader(file_name):
    line_set = set()
    file_in = open(file_name, "r")
    for line in file_in.read().splitlines():
        print(tuple(line.split("=", 2)))
        line_set.add(tuple(line.split("=", 2)))
    return line_set

replacements = replacement_reader("keywords/replacements.txt")

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
        if i != 0 and words[i][0].isupper():
            for j in range(i + 1, n - 1):
                if words[j][0].isupper():
                    new_words[-1] += words[j]
            i = j
        i += 1
    sentence = ' '.join(word for word in new_words)
    print(sentence)
    return sentence