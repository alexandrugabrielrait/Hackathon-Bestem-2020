try:
    from src.definitions import *
except:
    from definitions import *

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

client_synonyms = single_reader(CLIENT_SYN)
company_synonyms = single_reader(COMPANY_SYN)
permissive_verbs = multi_reader(PERMISSIVE_VERBS)
obligatory_verbs = multi_reader(OBLIGATORY_VERBS)
obligatory_verbs_constant = multi_reader(OBLIGATORY_VERBS_CONST)
replacements = replacement_reader(REPLACEMENTS)

company_name = ""

def get_company_synonyms():
    print(company_synonyms.union({company_name}))
    if company_name != "":
        return company_synonyms.union({company_name})
    return company_synonyms