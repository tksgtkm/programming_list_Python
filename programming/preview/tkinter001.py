from tkinter import Tk, Label, mainloop, Button
from tkinter.messagebox import showinfo
def reply():
    showinfo(title='pouup', message='Button pressed')
window = Tk()
button = Button(window, text='press', command=reply)
button.pack()
window.mainloop()