from src.file_names import *


def single_reader(file_name):
    line_set = set()
    file_in = open(file_name, "r")
    for line in file_in.read().splitlines():
        line_set.update(line.split())
    return line_set


def multi_reader(file_name):
    dictionary = {}
    file_in = open(file_name, "r")
    for line in file_in.read().splitlines():
        line = line.split()
        dictionary[line[0]] = line[1:]
    return dictionary


client_synonyms = single_reader(CLIENT_SYN)
company_synonyms = single_reader(COMPANY_SYN)
permissive_verbs = multi_reader(PERMISSIVE_VERBS)
obligatory_verbs = multi_reader(OBLIGATORY_VERBS)
obligatory_verbs_constant = multi_reader(CONST_OBLIGATORY_VERBS)

