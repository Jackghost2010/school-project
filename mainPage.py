try:    
    import tkinter as tk
    from random import randint
    from os import path
    from os import chdir
    from os import system
    import hashlib
    from logins import loginMain

    import socket
    import sqlite3


    connection = sqlite3.connect("users.db")


    cursor = connection.cursor()
    
    with open("users.db", "r") as usersdata:
        check = cursor.fetchone()
        if check:
            cursor.execute("create table users(username text,password text)")

        else:
            print("it already created")

    

    
        

        
        


    connection.close()

    loginMain()


except ImportError:
    print("Tkinter is not installed")