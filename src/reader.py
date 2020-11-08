try:
    from src.definitions import *
except:
    from definitions import *

'''
    Reads each line and puts it in a set
'''
def single_reader(file_name):
    line_set = set()
    file_in = open(file_name, "r")
    for line in file_in.read().splitlines():
        line_set.update(line.split())
    return line_set

'''
    Reads each line and adds it to a dictionary, using the first word as the key and the rest (auxiliary words) as the value
'''
def multi_reader(file_name):
    dictionary = {}
    file_in = open(file_name, "r")
    for line in file_in.read().splitlines():
        line = line.split()
        dictionary[line[0]] = line[1:]
    return dictionary


"""
    Reads each line and adds the 2 words separated by '=' to a set
"""
def replacement_reader(file_name):
    line_set = set()
    file_in = open(file_name, "r")
    for line in file_in.read().splitlines():
        line_set.add(tuple(line.split("=", 2)))
    return line_set

client_synonyms = single_reader(CLIENT_SYN)
company_synonyms = single_reader(COMPANY_SYN)
permissive_verbs = multi_reader(PERMISSIVE_VERBS)
obligatory_verbs = multi_reader(OBLIGATORY_VERBS)
obligatory_verbs_constant = multi_reader(OBLIGATORY_VERBS_CONST)
replacements = replacement_reader(REPLACEMENTS)

company_name = ""

'''
    Returns the synonyms for company, including the company name
'''
def get_company_synonyms():
    if company_name != "":
        return company_synonyms.union({company_name})
    return company_synonyms