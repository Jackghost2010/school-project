from random import randint
import sqlite3
from pathlib import Path
import hashlib
from os import system
from os import chdir
from getpass import getpass
from hashing import hashing_func

class user:
    def __init__(self,username,password,status = "user"):
        self.username = username
        self.password = password
        self.status = status

        self.checking = "The username: " + username + " The password is: " + password +" It is status " + status




def register_page():
    username = input("username: ")
    password = getpass("password: ")
    userinfor = user(username,hashing_func(password))








def check(directory,key):
    check_directory_exist = Path(directory)
    key_file_exist = Path(key)

    if check_directory_exist.is_dir():
        if key_file_exist.is_file():
            pass
        else:
            system("touch registeBefore")
            register_page()
    else:
        system(f"mkdir {directory}")
        chdir(f"{directory}")
    


