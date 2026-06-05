
from random import randint
import sqlite3
from pathlib import Path
from hashing import hashing_func
import register










def main():
    conn = sqlite3.connect("userdate.db")

    cursor = conn.cursor()
        
    
    cursor.execute("create table if not exists userinfo (username TEXT, password TEXT)")


    cursor.execute("select from useinfo")
    
    conn.close()
    
    
