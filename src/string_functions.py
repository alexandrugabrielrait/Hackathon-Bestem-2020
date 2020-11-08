transl_table = dict( [ (ord(x), ord(y)) for x,y in zip( u"‘’´“”–-",  u"'''\"\"--") ] )

'''
    Translates UTF-8 to ASCII
'''
def utf8_to_ascii(string):
    return string.translate(transl_table)

'''
    Translates cp1252 to ASCII
'''
def cp1252_to_ascii(string):
    return utf8_to_ascii(string.encode('cp1252').decode("utf-8"))