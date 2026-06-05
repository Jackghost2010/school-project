try:    
    import tkinter as tk
    from random import randint
    from os import path
    from os import chdir
    from os import system
    import hashlib
    import time
    import datetime
    import sqlite3

    def hashing(password):
        return str(hashlib.sha256(password.encode()).hexdigest())


        
    def submits(username,password):
        print(username,password)
        pass

    def register(root,username,password):

        root.title("register")  # Set the window title
        section = tk.Label(root, text="register").pack()


        username_labels = tk.Label(root,text="username").pack()  # Create a label
        username_entry = tk.Entry(root, textvariable = username).pack()
        password_labels = tk.Label(root,text="password").pack()  # Create a label

        password_entry = tk.Entry(root,textvariable = password ,show="*").pack()



        submit = tk.Button(root,text = "submit info")
        submit.config(command= submits(username,password))
        submit.config(command= root.destroy)
        submit.pack()

        escape = tk.Button(root,text = "exit",command= root.destroy).pack()


        canvas = tk.Canvas(root, height = 700, width = 500).pack()

    def registerMain():
        root = tk.Tk()  # Create the main window

        username_var = tk.StringVar()
        password_var = tk.StringVar()

        register(root,username_var,password_var)

        root.mainloop() 

    registerMain()

        
except ImportError:
    print("Tkinter is not installed")