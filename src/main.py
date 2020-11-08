from tkinter import *
try:
    from src.string_functions import utf8_to_ascii
    from src.data_functions import *
except:
    from string_functions import utf8_to_ascii
    from data_functions import *

def main():
    file_input = open("input.txt", "r", encoding='utf-8')
    sentences = find_sentences(utf8_to_ascii(file_input.read()))
    print(find_showable_list([True, False, True, True, True, False], sentences))

if __name__ == "__main__":
    main()
