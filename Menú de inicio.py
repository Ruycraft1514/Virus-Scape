from tkinter import *
import pygame

wn = Tk()
wn.geometry("720x720+0+0")
wn.configure(bg = 'blue')
wn.title("Start Menu")

#Image
img = PhotoImage(file = "background.gif")
lblImage = Label(wn, image = img).place(x = 0, y = 0)

#Functions
def open(file):
    file = open("Virus Scape 1.2.5.py")

def start():
    pass

def click_button():
    pass

if click_button ():
    pass

#Buttons
button1 = Button(wn, text = "PLAY", width =23, height = 5, command = lambda: open)
button1.configure(bg = 'blue')
boton1 = Button(wn, text = "1",width = 5, height = 2, command = lambda: start(1))
button1.grid(row = 4, column = 0, padx = 5, pady = 5)
button2 = Button(wn, text = "SETTINGS", width =23, height = 5)
button2.grid(row = 4, column = 1, padx = 5, pady = 5)
button2.configure(bg = 'red')
button3 = Button(wn, text = "RESTART GAME", width =23, height = 5)
button3.grid(row = 4, column = 2, padx = 5, pady = 5)
button3.configure(bg = 'green')
button4 = Button(wn, text = "EXIT", width =23, height = 5)
button4.grid(row = 4, column = 3, padx = 5, pady = 5)
button4.configure(bg = 'yellow')

wn.mainloop()
