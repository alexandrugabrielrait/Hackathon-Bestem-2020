from tkinter import *
try:
    from src.string_functions import utf8_to_ascii
    from src.data_functions import find_sets
except:
    from string_functions import utf8_to_ascii
    from data_functions import find_sets

def main():
    file_input = open("input.txt", "r", encoding='utf-8')
    find_sets(utf8_to_ascii(file_input.read()))

if __name__ == "__main__":
    main()
