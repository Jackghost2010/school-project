from random import randint
import sqlite3
from pathlib import Path
import ctype
def loginProccess():
    pass
def main():
    conn = sqlite3.connect("userdate.db")
    cursor = conn.cursor()
    cursor.execute("create table if not exists userinfo (username TEXT, password TEXT)")
    conn.close()
    
    


