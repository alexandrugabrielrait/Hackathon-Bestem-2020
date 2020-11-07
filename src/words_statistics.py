import nltk
from nltk import WordNetLemmatizer
from nltk.corpus import wordnet, stopwords

from src.simplify_functions import simplify

IN = "../inputs/github.txt"
OUT = "../outputs/github.txt"
text = open(IN).read().lower()

def get_wordnet_pos(word):
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}

    return tag_dict.get(tag, wordnet.NOUN)


def main_t2():
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words("english"))
    print("SW: " + str(stop_words))
    words = nltk.word_tokenize(text)
    lem_words = [lemmatizer.lemmatize(w, get_wordnet_pos(w)) for w in nltk.word_tokenize(text) if w.__len__() > 1]

    without_stop_words = [word for word in lem_words if not word in stop_words] # if not word.isalpha() and word.isnumeric()
    # print(without_stop_words)

    ss = simplify("a")


    statistic_dict = {}
    for word in without_stop_words:
        if word in statistic_dict:
            statistic_dict[word] += 1
        else:
            statistic_dict[word] = 1

    out_file = open(OUT, "w")
    for w in sorted(statistic_dict, key=statistic_dict.get, reverse=True):
        out_file.write(w + " " + str(statistic_dict[w]) + "\n")

    out_file.close()

    # for word, num in sorted statistic_dict.items():
    #     print(word + " : " + str(num))

if __name__ == "__main__":
    main_t2()
