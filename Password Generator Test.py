import random
import array
 
LENGTH = 12

DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']
 
UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']
 
SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<']
 
COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS

rand_digit = random.choice(DIGITS)
rand_upper = random.choice(UPCASE_CHARACTERS)
rand_lower = random.choice(LOCASE_CHARACTERS)
rand_symbol = random.choice(SYMBOLS)

temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol
 

for x in range(LENGTH-4):
    temp_pass = temp_pass + random.choice(COMBINED_LIST)
 
    temp_pass_list = array.array('u', temp_pass)
    random.shuffle(temp_pass_list)
 
password = ""
for x in temp_pass_list:
        password = password + x

from tkinter import *
import tkinter.font as font

def printSomething():

        label = Label(root, text= str(password))
        label.config(font =("Arial", 16, 'bold'))
        label.pack()
        label.place(relx=0.5, rely=0.56, anchor=CENTER)

root = Tk()

myFont=font.Font(size=14,family="Arial")

l = Label(root, text= "Password Genertaor")
l.config(font =("Arial", 32, 'bold'))
l.pack()

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.state('zoomed')

button = Button(root, text="Generate Password", command=printSomething, height=1, width=18, font=myFont) 
button.pack()
button.place(relx=0.5, rely=0.5, anchor=CENTER)

m = Label(root, text= "Made by-")
m.config(font =("Arial", 22, 'bold'))
m.pack()
m.place(relx=0.5, rely=0.7, anchor=CENTER)

r = Label(root, text= "Rudraksh Parmar")
r.config(font =("Arial", 18))
r.pack()
r.place(relx=0.5, rely=0.75, anchor=CENTER)

y = Label(root, text= "Yug Savani")
y.config(font =("Arial", 18))
y.pack()
y.place(relx=0.5, rely=0.79, anchor=CENTER)

d = Label(root, text= "Dhwani Navadia")
d.config(font =("Arial", 18))
d.pack()
d.place(relx=0.5, rely=0.83, anchor=CENTER)

root.mainloop()
