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
    from registers import registerMain

    def hashing(password):
        return str(hashlib.sha256(password.encode()).hexdigest())
        

        
    def submits():
        username = username_var.get()
        Password = password_var.get()


        connection = sqlite3.connect("users.db")

        cursor = connection.cursor()
        




    def login(root,username,password):
        root.title("login")  # Set the window title

        username_labels = tk.Label(root,text="username").pack()  # Create a label
        username_entry = tk.Entry(root, textvariable = username).pack()
        password_labels = tk.Label(root,text="password").pack()  # Create a label

        password = tk.Entry(root,textvariable = password ,show="*").pack()



        submit = tk.Button(root,text = "submit info",command = submits).pack()

        notHaveUserName = tk.Button(root,text="don't have any account!")

        notHaveUserName.config(command= registerMain())
        notHaveUserName.config(root.destroy)
        notHaveUserName.pack()


        escape = tk.Button(root,text = "exit",command= root.destroy).pack()


        canvas = tk.Canvas(root, height = 700, width = 500).pack()
        
    def loginMain():
        root = tk.Tk()  # Create the main window

        username_var = tk.StringVar()
        password_var = tk.StringVar()
        
        login(root,username_var,password_var)

        root.mainloop() 

    loginMain()
except ImportError:
    print("Tkinter is not installed")