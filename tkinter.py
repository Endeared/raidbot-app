from tkinter import *

root = Tk()
root.geometry('300x400')
mybutton = Button(root, text='Hello World!', font=('Inter', 14))
mybutton.place(relx=0.5, rely=0.5, anchor=CENTER)
root.mainloop()