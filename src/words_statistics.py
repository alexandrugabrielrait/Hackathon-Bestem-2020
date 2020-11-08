import nltk
from nltk import WordNetLemmatizer
from nltk.corpus import wordnet, stopwords
import matplotlib.pyplot as plt


IN = "../inputs/github.txt"
OUT = "../outputs/github.txt"
text2 = open(IN).read().lower()

MIN_FACTOR = 0.03
MAX = 15


def get_wordnet_pos(word):
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}

    return tag_dict.get(tag, wordnet.NOUN)


def word_statistics(text):
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words("english"))
    # words = nltk.word_tokenize(text)
    lem_words = [lemmatizer.lemmatize(w, get_wordnet_pos(w)) for w in nltk.word_tokenize(text) if w.__len__() > 1]

    without_stop_words = [word for word in lem_words if
                          not word in stop_words]  # if not word.isalpha() and word.isnumeric()


    statistic_dict = {}
    for word in without_stop_words:
        if word in statistic_dict:
            statistic_dict[word] += 1
        else:
            statistic_dict[word] = 1

    out_file = open(OUT, "w")

    sorted_stat = sorted(statistic_dict, key=statistic_dict.get, reverse=True)

    values = []
    keys = []

    # min_limit = sorted_stat.__len__() * MIN_FACTOR
    if MAX > sorted_stat.__len__() / 2:
        max = int(sorted_stat.__len__() / 2)
    else:
        max = MAX
    for w in sorted_stat[0:max]:
        # if statistic_dict[w] > min_limit:
            values.append(w)
            keys.append(statistic_dict[w])

    plt.bar(values, keys)
    plt.xticks(rotation=45)
    plt.gcf().subplots_adjust(bottom=0.2)
    plt.show()

    for w in sorted_stat:
        out_file.write(w + " " + str(statistic_dict[w]) + "\n")

    out_file.close()


# if __name__ == "__main__":
    # word_statistics(text2)
