try:    
    import tkinter as tk
    from random import randint
    from os import path
    from os import chdir
    from os import system
    import hashlib



    def submits(username):

        with open("text.txt", "w") as file:
            file.write()

    
    def register(root):

        root.title("register")  # Set the window title
        canvas = tk.Canvas(root,height = 500, width = 700).pack()
        section = tk.Label(root, text="register").pack()


        username_labels = tk.Label(root,text="username").pack()  # Create a label
        username = tk.Entry(root).pack()
        password_labels = tk.Label(root,text="password").pack()  # Create a label
        password = tk.Entry(root,show="*").pack()

        submit = tk.Button(root,text="submit information" ).pack()




        exited = tk.Button(root,text="exit the code",command="destroy.root").pack()









        


    def login(root):
        root.title("login")  # Set the window title
        canvas = tk.Canvas(root,height = 500, width = 700)
        label = tk.Label(root, text="login")  # Create a label
        label.pack()  # Add the label to the window
        canvas.pack()


    def mainPage(root):

        root = tk.Tk()
        canvas = tk.Canvas(root).pack()
        label = tk.Label(root, text="works").pack()

        root.mainloop() 


    def main():
            
        root = tk.Tk()  # Create the main window

        with open("check.txt", "r") as f:
            if f.read() == "":
                register(root)
            else:
                login(root)


        root.mainloop()  # Start the Tkinter event loop
    main()
        
        
        
except ImportError:
    print("Tkinter is not installed")
