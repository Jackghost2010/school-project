import tkinter as tk
from os import system
from os import chdir
from random import randint

"""
this is how to create a title
label = tk.Label(root,text = "login screen")

label.pack()

buttom 

root = tk.Tk()
root.title("Counting Seconds")

button = tk.Button(root, text="Stop", width=25, command=root.destroy)
button.pack()

root.mainloop()

"""

root = tk.Tk()

label = tk.Label(root,text = "login screen", width= 140)


button = tk.Button(root, text="Stop", width=25, command=root.destroy)
label.pack()

button.pack()



root.mainloop()

