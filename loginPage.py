try:    
    import tkinter as tk
    from random import randint
    from os import path
    from os import chdir
    from os import system
    import hashlib

    def hashing(password):
        return str(hashlib.sha256(password.encode()).hexdigest())
        

        
    def submits():
        username = username_var.get()
        Password = password_var.get()
        

        with open("check.txt", "w") as file:
            file.write(username + "\n")
            file.write(str(hashing(Password)) + "\n")



        

    
    def register(root):

        root.title("register")  # Set the window title
        section = tk.Label(root, text="register").pack()


        username_labels = tk.Label(root,text="username").pack()  # Create a label
        username_entry = tk.Entry(root, textvariable = username_var).pack()
        password_labels = tk.Label(root,text="password").pack()  # Create a label

        password = tk.Entry(root,textvariable = password_var ,show="*").pack()



        submit = tk.Button(root,text = "submit info",command = submits).pack()

        escape = tk.Button(root,text = "exit",command= root.destroy).pack()


        canvas = tk.Canvas(root, height = 700, width = 500).pack()



    def login(root):
        root.title("login")  # Set the window title

        label = tk.Label(root, text="login").pack()  # Create a label

        canvas = tk.Canvas(root,height = 500, width = 700).pack()

    def mainPage(root):

        root = tk.Tk()
        canvas = tk.Canvas(root).pack()
        label = tk.Label(root, text="works").pack()

        root.mainloop()


    root = tk.Tk()  # Create the main window

    username_var = tk.StringVar()
    password_var = tk.StringVar()

    with open("check.txt", "r") as f:

        
        
        register(root)

    root.mainloop() 


        
        
        
except ImportError:
    print("Tkinter is not installed")
