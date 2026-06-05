from random import randint
import sqlite3
from pathlib import Path
import hashlib
from os import system
from os import chdir

def register_page():
    
    user = input("name: ")


    password = getpass("password: ")


    hashing_func(password)

    pass
