#The tkinter.filedialog module provides classes and factory functions for creating file/directory selection windows.
#tkinter is used for creating the GUI applications in Python.
from tkinter.filedialog import *
import tkinter as tk

#to save file with the address and format with write mode
def savefile():
    new_file = asksaveasfile(mode = 'w',filetype = [('text files','*.txt')])
    if new_file is None:
        return
    text = str(entry.get(1.0, tk.END))
    new_file.write(text)
    new_file.close()

#to open file with the address and format with read mode

def openfile():
    file = askopenfile(mode = 'r',filetype = [('text files','*.txt')])
    if file is not None:
        content = file.read()
    entry.insert(tk.INSERT, content)

#to delete or clear the dataa entered

def clearfile():
    entry.delete(1.0 , tk.END)

#format with the design and geometry

canvas = tk.Tk()
canvas.geometry("400x600")
canvas.title("Notepad")
canvas.config(bg = "black")

top = tk.Frame(canvas)

top.pack(padx=10,pady=5,anchor='nw')

#adding Buttons in Notepad

b1 = tk.Button(canvas, text = "Open", bg = 'white',command = openfile)
b1.pack(in_ = top,side='left')

b2 = tk.Button(canvas, text = "Save", bg = 'white',command = savefile)
b2.pack(in_ = top,side='left')

b3 = tk.Button(canvas, text = "Clear", bg = 'white',command = clearfile)
b3.pack(in_=top,side='left')

b4 = tk.Button(canvas, text = "Exit", bg = 'white',command = exit)
b4.pack(in_ = top,side='left')

entry = tk.Text(canvas,wrap = tk.WORD, bg = "#F9DDA4", font = ("poppins",15))
entry.pack(padx = 10,pady =5,expand = tk.TRUE, fill = tk.BOTH)


canvas.mainloop()