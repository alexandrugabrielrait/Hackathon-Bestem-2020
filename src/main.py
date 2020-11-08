import tkinter as tk
from tkinter import *
from tkinter.scrolledtext import ScrolledText
import sqlite3
try:
    from src.string_functions import utf8_to_ascii
    from src.data_functions import *
    from src.words_statistics import word_statistics
except:
    from string_functions import utf8_to_ascii
    from data_functions import *
    from words_statistics import word_statistics
from tkinter import messagebox as MessageBox

show_client = True
show_company = True
show_obligatory = True
show_permissive = True
show_neutral = True
show_rest = True
show_definitions = False
input_mode = True
save = ""
text_input = "Input EULA here"
text_result = "Results"

search_list = list()
ss = ""

def toggle_input_mode(s, e, L):
    global input_mode, save, ss
    ss = ""
    input_mode = not input_mode
    if not input_mode:
        L.config(text = text_result)
        s.bind("<1>", lambda event: s.focus_set())
        save = s.get('0.0', 'end-1c')
        print_info(s, e)
    else:
        L.config(text = text_input)
        s.delete("0.0", tk.END)
        s.insert(INSERT, save)


def editarelabel1(LL):
    LL.config(text="INTRODUCETI ALTI TERMENI")


def editare1(s):
    s.delete("0.0", tk.END)


def editarelabel2(LL):
    LL.config(text="TERMENII IMPORTANTI!!")


def editare2(s):
    mytext = StringVar()
    mytext = s.get('0.0', 'end-1c')
    s.delete("0.0", tk.END)
    s.insert(INSERT, mytext)


def filtru(s, number):
    sir = ""
    f = open("database.txt", "r")
    sir = f.read()
    prop = sir.split('.', 4)
    f.close()

    s.delete("0.0", tk.END)
    if number == 5:
        s.insert(INSERT, sir)
    else:
        s.insert(INSERT, prop[number])
    return s


def reset_list(p, source):
    if ss != p.get():
        search_list.clear()
        source.tag_remove(SEL, 1.0, "end-1c")



def search_words(p, source):
    reset_list(p, source)
    global search_list
    global ss
    source.focus_set()
    ss = p.get()

    if ss:
        if not search_list:
            idx = "1.0"
        else:
            idx = search_list[-1]

        idx = source.search(ss, idx, nocase=1, stopindex=END)
        lastidx = '%s+%dc' % (idx, len(ss))

        try:
            source.tag_remove(SEL, 1.0, lastidx)
        except:
            pass

        try:
            source.tag_add(SEL, idx, lastidx)
            counter_list = str(idx).split('.')
            source.mark_set("insert", "%d.%d" % (float(int(counter_list[0])), float(int(counter_list[1]))))
            source.see(float(int(counter_list[0])))
            search_list.append(lastidx)
        except:
            MessageBox.showinfo("Search complete", "No further matches")
            search_list.clear()
            source.tag_remove(SEL, 1.0, "end-1c")

def clear(s, e, L):
    global save
    s.delete("0.0", tk.END)
    save = ""

def toggle_client(s):
    global show_client
    show_client = not show_client


def toggle_company(s):
    global show_company
    show_company = not show_company


def toggle_obligatory(s):
    global show_obligatory
    show_obligatory = not show_obligatory


def toggle_permissive(s):
    global show_permissive
    show_permissive = not show_permissive


def toggle_neutral(s):
    global show_neutral
    show_neutral = not show_neutral


def toggle_rest(s):
    global show_rest
    show_rest = not show_rest


def toggle_definitions(s):
    global show_definitions
    show_definitions = not show_definitions

def print_statistics(s):
    if input_mode:
        word_statistics(s.get('0.0', END))
    else:
        word_statistics(save)

def print_info(s, e):
    global ss
    ss = ""
    set_company_name(e.get().lower())
    if (input_mode):
        return
    s.delete("0.0", tk.END)
    if show_definitions:
        s.insert(END, "The following definitions have been found:\n")
        for definition in find_definitions(utf8_to_ascii(save)):
            s.insert(END, '"' + definition + '"\n')
    else:
        sentences = find_sentences(utf8_to_ascii(save))
        for sentence in find_showable_list([show_client, show_company, show_rest, show_permissive, show_neutral, show_obligatory], sentences):
            s.insert(END, sentence + "\n")

def ecran():
    mainwin = Tk()
    mainwin.geometry("1920x1080")
    mainwin.title('Terms and Conditions Inspector')

    L1 = Label(mainwin, text=text_input, font=("Helvetica", 16))
    L1.pack()

    s = ScrolledText(mainwin, width=185, height=40)
    s.pack()

    L2 = Label(mainwin, text="Type word to find in text:", font=("Helvetica", 12))
    L2.pack(anchor="n")
    e1 = Entry(mainwin, width=30)
    e1.pack(anchor="n")
    L3 = Label(mainwin, text="Type company name:", font=("Helvetica", 12))
    L3.pack(anchor="n")
    e2 = Entry(mainwin, width=30)
    e2.pack(anchor="n")
    b1 = Button(command=lambda: clear(s, e2, L1), text="Clear", activebackground="grey",
                bg="red", bd=5, padx=20)
    b3 = tk.Checkbutton(width=15, text="Client", indicatoron=True, selectcolor="grey", background="white",
                        command=lambda: toggle_client(s))
    b4 = tk.Checkbutton(width=15, text="Company", indicatoron=True, selectcolor="grey", background="white",
                        command=lambda: toggle_company(s))
    b5 = tk.Checkbutton(width=15, text="Rest", indicatoron=True, selectcolor="grey", background="white",
                        command=lambda: toggle_rest(s))
    b6 = tk.Checkbutton(width=15, text="Permissive", indicatoron=True, selectcolor="grey", background="white",
                        command=lambda: toggle_permissive(s))
    b7 = tk.Checkbutton(width=15, text="Neutral", indicatoron=True, selectcolor="grey", background="white",
                        command=lambda: toggle_neutral(s))
    b8 = tk.Checkbutton(width=15, text="Obligatory", indicatoron=True, selectcolor="grey", background="white",
                        command=lambda: toggle_obligatory(s))

    b9 = Button(mainwin, command=lambda: search_words(e1, s), text="FIND", activebackground="grey", bg="white", bd=5,
                padx=20)

    b3.toggle()
    b4.toggle()
    b5.toggle()
    b6.toggle()
    b7.toggle()
    b8.toggle()

    b10 = tk.Checkbutton(width=15, text="Edit/Results", indicatoron=False, selectcolor="lightblue",
                         background="white", command=lambda: toggle_input_mode(s, e2, L1))
    b11 = tk.Checkbutton(width=15, text="Show Definitions", indicatoron=False, selectcolor="lightblue", background="white",
                         command=lambda: toggle_definitions(s))

    b12 = tk.Button(width=15, text="Show Statistics", background="white",
                         command=lambda: print_statistics(s))

    b13 = Button(mainwin, command=lambda: print_info(s, e2), text="FILTER", activebackground="grey", bg="white", bd=5,
                padx=20)

    top = 690
    middle = 735
    bottom = 780
    x0 = 1100
    x1 = x0 + 150
    x2 = x1 + 150

    b1.place(x=750, y=bottom)
    b3.place(x=x0, y=top)
    b4.place(x=x1, y=top)
    b5.place(x=x2, y=top)
    b6.place(x=x0, y=middle)
    b7.place(x=x1, y=middle)
    b8.place(x=x2, y=middle)
    b9.place(x=750, y=top)
    b10.place(x=900, y=bottom)
    b11.place(x=x0, y=bottom)
    b12.place(x=x1, y=bottom)
    b13.place(x=750, y=middle)

    mainwin.mainloop()


if __name__ == "__main__":
    ecran()
