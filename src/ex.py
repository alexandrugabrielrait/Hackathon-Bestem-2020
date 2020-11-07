import tkinter as tk
from tkinter import *
from tkinter.scrolledtext import ScrolledText
import sqlite3

show_client = True
show_company = True
show_obligatory = True
show_permissive = True
show_neutral = True
show_rest = True

def editarelabel1(LL):
	LL.config(text="INTRODUCETI ALTI TERMENI")
	#return LL

def editare1(s):
	s.delete("0.0",tk.END)
	#return s

def editarelabel2(LL):
	LL.config(text="TERMENII IMPORTANTI!!")
	#return LL

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
	
	
def toggle_client(s,b3):
	global show_client
	show_client = not show_client
	s.delete("0.0",tk.END)
	f = open("database.txt", "r")
	sir = f.read()
	prop = sir.split('.',5)
	if show_client == True:
			s.insert(END, prop[0])
			s.insert(END, " ")
	if show_company == True:
			s.insert(END, prop[1])
			s.insert(END, " ")	
	if show_obligatory == True:
			s.insert(END, prop[2])
			s.insert(END, " ")
	if show_permissive == True:
			s.insert(END, prop[3])
			s.insert(END, " ")
	if show_neutral == True:
			s.insert(END, prop[4])
			s.insert(END, " ")
	if show_rest == True:
			s.insert(END, prop[5])
			s.insert(END, " ")		
				
def toggle_company(s,b4):
	global show_company
	show_company = not show_company
	s.delete("0.0",tk.END)
	f = open("database.txt", "r")
	sir = f.read()
	prop = sir.split('.',5)
	if show_client == True:
			s.insert(END, prop[0])
			s.insert(END, " ")
	if show_company == True:
			s.insert(END, prop[1])
			s.insert(END, " ")	
	if show_obligatory == True:
			s.insert(END, prop[2])
			s.insert(END, " ")
	if show_permissive == True:
			s.insert(END, prop[3])
			s.insert(END, " ")
	if show_neutral == True:
			s.insert(END, prop[4])
			s.insert(END, " ")
	if show_rest == True:
			s.insert(END, prop[5])
			s.insert(END, " ")		

def toggle_obligatory(s,b5):
	global show_obligatory
	show_obligatory = not show_obligatory
	s.delete("0.0",tk.END)
	f = open("database.txt", "r")
	sir = f.read()
	prop = sir.split('.',5)
	if show_client == True:
			s.insert(END, prop[0])
			s.insert(END, " ")
	if show_company == True:
			s.insert(END, prop[1])
			s.insert(END, " ")	
	if show_obligatory == True:
			s.insert(END, prop[2])
			s.insert(END, " ")
	if show_permissive == True:
			s.insert(END, prop[3])
			s.insert(END, " ")
	if show_neutral == True:
			s.insert(END, prop[4])
			s.insert(END, " ")
	if show_rest == True:
			s.insert(END, prop[5])
			s.insert(END, " ")	

def toggle_permissive(s,b6):
	global show_permissive
	show_permissive = not show_permissive
	s.delete("0.0",tk.END)
	f = open("database.txt", "r")
	sir = f.read()
	prop = sir.split('.',5)
	if show_client == True:
			s.insert(END, prop[0])
			s.insert(END, " ")
	if show_company == True:
			s.insert(END, prop[1])
			s.insert(END, " ")	
	if show_obligatory == True:
			s.insert(END, prop[2])
			s.insert(END, " ")
	if show_permissive == True:
			s.insert(END, prop[3])
			s.insert(END, " ")
	if show_neutral == True:
			s.insert(END, prop[4])
			s.insert(END, " ")
	if show_rest == True:
			s.insert(END, prop[5])
			s.insert(END, " ")		

def toggle_neutral(s,b7):
	global show_neutral
	show_neutral = not show_neutral
	s.delete("0.0",tk.END)
	f = open("database.txt", "r")
	sir = f.read()
	prop = sir.split('.',5)
	if show_client == True:
			s.insert(END, prop[0])
			s.insert(END, " ")
	if show_company == True:
			s.insert(END, prop[1])
			s.insert(END, " ")	
	if show_obligatory == True:
			s.insert(END, prop[2])
			s.insert(END, " ")
	if show_permissive == True:
			s.insert(END, prop[3])
			s.insert(END, " ")
	if show_neutral == True:
			s.insert(END, prop[4])
			s.insert(END, " ")
	if show_rest == True:
			s.insert(END, prop[5])
			s.insert(END, " ")		

def toggle_rest(s,b8):
	global show_rest
	show_rest = not show_rest
	s.delete("0.0",tk.END)
	f = open("database.txt", "r")
	sir = f.read()
	prop = sir.split('.',5)
	if show_client == True:
			s.insert(END, prop[0])
			s.insert(END, " ")
	if show_company == True:
			s.insert(END, prop[1])
			s.insert(END, " ")	
	if show_obligatory == True:
			s.insert(END, prop[2])
			s.insert(END, " ")
	if show_permissive == True:
			s.insert(END, prop[3])
			s.insert(END, " ")
	if show_neutral == True:
			s.insert(END, prop[4])
			s.insert(END, " ")
	if show_rest == True:
			s.insert(END, prop[5])
			s.insert(END, " ")				
	
def ecran():
	mainwin = Tk()
	mainwin.geometry("1080x1920")
	
	L1 = Label(mainwin, text="Introduceti textul aici", font=("Helvetica", 16))
	L1.pack()
	
	s = ScrolledText(mainwin, width=185, height=40)
	s.pack()
	
	b1 = Button (command=lambda: [editare1(s), editarelabel1(L1), separare(s)], text="Delete",activebackground="white",bg="grey",bd=5,padx=20)
	b2 = Button (command=lambda: [editare2(s), editarelabel2(L1), separare(s)], text="Editare",activebackground="white",bg="grey",bd=5,padx=20)
	b1.pack(side=LEFT)
	b2.pack(side=LEFT)
	
	#b3 = Button(command=lambda: filtru(s,0), text="Client",activebackground="grey",bg="white",bd=5,padx=20)
	#b4 = Button(command=lambda: filtru(s,1), text="Company",activebackground="grey",bg="white",bd=5,padx=20)
	#b5 = Button(command=lambda: filtru(s,2), text="Obligatory",activebackground="grey",bg="white",bd=5,padx=20)
	#b6 = Button(command=lambda: filtru(s,3), text="Permisive",activebackground="grey",bg="white",bd=5,padx=20)
	#b7 = Button(command=lambda: filtru(s,4), text="Remaining",activebackground="grey",bg="white",bd=5,padx=20)
	#b8 = Button(command=lambda: filtru(s,5), text="All",activebackground="grey",bg="white",bd=5,padx=20)
	#b8.pack(side=RIGHT)
	#b7.pack(side=RIGHT)
	#b6.pack(side=RIGHT)
	#b5.pack(side=RIGHT)
	#b4.pack(side=RIGHT)
	#b3.pack(side=RIGHT)
	
	L2 = Label(mainwin, text="Introduceti textul aici", font=("Helvetica", 12))
	L2.pack()
	e1 = Entry(mainwin)
	e1.pack()
	b9 = Button(command=lambda: gasire(e1,s), text="FIND",activebackground="grey",bg="white",bd=5,padx=20)
	b9.pack()
	var3 = tk.StringVar()
	var3 = "Client"
	var4 = tk.StringVar()
	var4 = "Company"
	var5 = tk.StringVar()
	var5 = "Obligatory"
	var6 = tk.StringVar()
	var6 = "Permissive"
	var7 = tk.StringVar()
	var7 = "Neutral"
	var8 = tk.StringVar()
	var8 = "Rest"
	b3 = tk.Checkbutton(width=8,height=5,variable=var3, textvariable=var3,indicatoron=True, selectcolor="grey", background="white",onvalue="Client", offvalue="Client",command=lambda: toggle_client(s,b3))
	b4 = tk.Checkbutton(width=8,height=5,variable=var4, textvariable=var4,indicatoron=True, selectcolor="grey", background="white",onvalue="Company", offvalue="Company",command=lambda: toggle_company(s,b4))
	b5 = tk.Checkbutton(width=8,height=5,variable=var5, textvariable=var5,indicatoron=True, selectcolor="grey", background="white",onvalue="Obligatory", offvalue="Obligatory",command=lambda: toggle_obligatory(s,b5))
	b6 = tk.Checkbutton(width=8,height=5,variable=var6, textvariable=var6,indicatoron=True, selectcolor="grey", background="white",onvalue="Permissive", offvalue="Permissive",command=lambda: toggle_permissive(s,b6))
	b7 = tk.Checkbutton(width=8,height=5,variable=var7, textvariable=var7,indicatoron=True, selectcolor="grey", background="white",onvalue="Neutral", offvalue="Neutral",command=lambda: toggle_neutral(s,b7))
	b8 = tk.Checkbutton(width=8,height=5,variable=var8, textvariable=var8,indicatoron=True, selectcolor="grey", background="white",onvalue="Rest", offvalue="Rest",command=lambda: toggle_rest(s,b8))
	b8.pack(side=RIGHT)
	b7.pack(side=RIGHT)
	b6.pack(side=RIGHT)
	b5.pack(side=RIGHT)
	b4.pack(side=RIGHT)
	b3.pack(side=RIGHT)
	
	mainwin.mainloop()
 
if __name__ == "__main__":
	ecran()
	
