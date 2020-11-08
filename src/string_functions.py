try:
    from src.reader import replacements
except:
    from reader import replacements

transl_table = dict( [ (ord(x), ord(y)) for x,y in zip( u"‘’´“”–-",  u"'''\"\"--") ] )

def utf8_to_ascii(string):
    return string.translate(transl_table)

def cp1252_to_ascii(string):
    return utf8_to_ascii(string.encode('cp1252').decode("utf-8"))