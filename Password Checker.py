open1 = open("Password.txt", "r")
password = (open1.read())

from tkinter import *
import tkinter.font as font


frame = Tk()
frame.title("Password Checker")
frame.geometry('1200x700')
frame.state('zoomed')

l = Label(frame, text= "Password Checker")
l.config(font =("Arial", 32, 'bold'))
l.pack()

myFont=font.Font(size=14,family="Arial")
  
def printInput():
    inp = inputtxt.get(1.0, "end-1c")
    check= (inp== password)
    
    if check== True:
        lbl.config(text = "Password is Correct", fg="green", font =("Arial", 16, 'bold'))
        lbl.place(relx=0.5, rely=0.6, anchor=CENTER)

    else:
        lbl.config(text = "Password is Incorrect", fg="red", font =("Arial", 16, 'bold'))
        lbl.place(relx=0.5, rely=0.6, anchor=CENTER)
        
inputtxt = Text(frame, height = 1, width = 16, padx=6, pady=8)
inputtxt.pack()
  

printButton = Button(frame, text = "Check Password", command = printInput, font=myFont)
printButton.pack()
printButton.place(relx=0.5, rely=0.5, anchor=CENTER)
  
lbl = Label(frame, text = "")
lbl.pack()

m = Label(frame, text= "Made by-")
m.config(font =("Arial", 22, 'bold'))
m.pack()
m.place(relx=0.5, rely=0.7, anchor=CENTER)

r = Label(frame, text= "Rudraksh Parmar")
r.config(font =("Arial", 18))
r.pack()
r.place(relx=0.5, rely=0.75, anchor=CENTER)

frame.mainloop()
