import tkinter as tk
from tkinter import *
from tkinter.scrolledtext import ScrolledText
import sqlite3
from string_functions import utf8_to_ascii
from pseudo_data_functions import *

show_client = True
show_company = True
show_obligatory = True
show_permissive = True
show_neutral = True
show_rest = True
show_definitions = True
input_mode = True
save = ""

def toggle_input_mode(s):
	global input_mode, save
	input_mode = not input_mode
	print(input_mode)
	if not input_mode:
		s.bind("<1>", lambda event: s.focus_set())
		save = s.get('0.0', 'end-1c')
		show_sets(s)
	else:
		s.delete("0.0",tk.END)
		s.insert(INSERT, save)
		
def editarelabel1(LL):
	LL.config(text="INTRODUCETI ALTI TERMENI")

def editare1(s):
	s.delete("0.0",tk.END)

def editarelabel2(LL):
	LL.config(text="TERMENII IMPORTANTI!!")

def editare2(s):
	mytext = StringVar()
	mytext = s.get('0.0', 'end-1c')
	s.delete("0.0",tk.END)
	s.insert(INSERT, mytext)

def filtru(s,number):
	sir = ""
	f = open("database.txt", "r")
	sir = f.read()
	prop = sir.split('.',4)
	f.close()
	
	s.delete("0.0",tk.END)
	if number == 5:
		s.insert(INSERT,sir)
	else:
		s.insert(INSERT,prop[number])
	return s
	
def gasire(e1,s):
		pattern = StringVar()
		sir = StringVar()
		pattern = e1.get().lower()
		sir = s.get('1.0', 'end-1c')
		s.delete("0.0",tk.END)
		lines = sir.splitlines()
		i = -1
		index = END
		first = True
		for line in lines:
			if first:
				first = False
			else:
				s.insert(END, " ")
			is_part = [False] * len(line)
			try: 
				i = line.lower().index(pattern)
				while True:
					print(i)
					for j in range(i,i+len(pattern)):
						is_part[j] = True
					i += 1+line[i+1:].lower().index(pattern)
			except:
				pass
			for i in range(len(line)):
				if is_part[i]:
					s.insert(END, line[i], 'da')
				else:
					s.insert(END, line[i], 'nu')
			first = True
			s.insert(END, "\n")	
				
		s.tag_config('da',foreground='red')		
				
		
def separare(s):
	sir = s.get('0.0', 'end-1c')
	f = open("database.txt", "w")
	f.write(sir)
	f.close()
	
	
def toggle_client(s):
	global show_client
	show_client = not show_client
	show_sets(s)		
				
def toggle_company(s):
	global show_company
	show_company = not show_company
	show_sets(s)

def toggle_obligatory(s):
	global show_obligatory
	show_obligatory = not show_obligatory
	show_sets(s)

def toggle_permissive(s):
	global show_permissive
	show_permissive = not show_permissive
	show_sets(s)

def toggle_neutral(s):
	global show_neutral
	show_neutral = not show_neutral
	show_sets(s)		

def toggle_rest(s):
	global show_rest
	show_rest = not show_rest
	show_sets(s)

def toggle_definitions(s):
	global show_definitions
	show_definitions = not show_definitions
	show_sets(s)
	
def show_sets(s):
	s.delete("0.0",tk.END)
	sentences = find_sentences(utf8_to_ascii(save))
	for sentence in find_showable_list([show_client,show_company, show_rest, show_permissive, show_neutral, show_obligatory], sentences):
		s.insert(END, sentence+"\n")	
	if show_definitions:
		s.insert(END,"\nThe following definitions have been found:\n")
		for definition in find_definitions(utf8_to_ascii(save)):
			s.insert(END, '"'+definition+'"\n')
	
def ecran():
	mainwin = Tk()
	mainwin.geometry("1920x1080")
	
	L1 = Label(mainwin, text="Introduceti textul aici", font=("Helvetica", 16))
	L1.pack()
	
	s = ScrolledText(mainwin, width=185, height=40)
	s.pack()
	
	L2 = Label(mainwin, text="Introduceti textul aici", font=("Helvetica", 12))
	L2.pack(anchor="n")
	e1 = Entry(mainwin,width=30)
	e1.pack(anchor="n")
	b1 = Button (command=lambda: [editare1(s), editarelabel1(L1), separare(s)], text="Delete",activebackground="white",bg="grey",bd=5,padx=20)
	b2 = Button (command=lambda: [editare2(s), editarelabel2(L1), separare(s)], text="Editare",activebackground="white",bg="grey",bd=5,padx=20)
	b3 = tk.Checkbutton(width=15,text="Client",indicatoron=True, selectcolor="grey", background="white",command=lambda: toggle_client(s))
	b4 = tk.Checkbutton(width=15,text="Company",indicatoron=True, selectcolor="grey", background="white",command=lambda: toggle_company(s))
	b5 = tk.Checkbutton(width=15,text="Rest",indicatoron=True, selectcolor="grey", background="white",command=lambda: toggle_rest(s))
	b6 = tk.Checkbutton(width=15,text="Permissive",indicatoron=True, selectcolor="grey", background="white",command=lambda: toggle_permissive(s))
	b7 = tk.Checkbutton(width=15,text="Neutral",indicatoron=True, selectcolor="grey", background="white",command=lambda: toggle_neutral(s))
	b8 = tk.Checkbutton(width=15,text="Obligatory",indicatoron=True, selectcolor="grey", background="white",command=lambda: toggle_obligatory(s))
	b1.place(x=30,y=700)
	b2.place(x=130,y=700)

	b9 = Button(mainwin,command=lambda: gasire(e1,s), text="FIND",activebackground="grey",bg="white",bd=5,padx=20)
	b9.place(x=735,y=725)
	b5.place(x=1300,y=700)
	b4.place(x=1150,y=700)
	b3.place(x=1000,y=700)
	b8.place(x=1300,y=750)
	b7.place(x=1150,y=750)
	b6.place(x=1000,y=750)
	
	b3.toggle()
	b4.toggle()
	b5.toggle()
	b6.toggle()
	b7.toggle()
	b8.toggle()
	
	b10 = tk.Checkbutton(width=15,onvalue="Edit",offvalue="Filter",indicatoron=False, selectcolor="grey", background="white",command=lambda: toggle_input_mode(s))
	b10.place(x=835,y=725)
	
	b11 = tk.Checkbutton(width=15,text="Show Definitions",indicatoron=True, selectcolor="grey", background="white",command=lambda: toggle_definitions(s))
	b11.place(x=580,y=725)
	mainwin.mainloop()
 
if __name__ == "__main__":
	ecran()
	
