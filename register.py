try:
    from random import randint
    import sqlite3
    from pathlib import Path
    from os import system
    from os import chdir
    from getpass import getpass
    from hashing import hashing_func
    from classes import user

    def register_page():
        conn = sqlite3.connect("userdata.db")
        
        username = input("username: ")
        password = getpass("password: ")
        userinfor = user(username,hashing_func(password))
        print(userinfor.username, userinfor.password, userinfor.status)
        
        
        
    def check():
        
        directory = "key_directory"
        key = "being_here_before"
        
        check_directory_exist = Path(directory)
        check_key_exist = Path(f"\/{directory}\/{key}")
        if check_directory_exist.is_dir():
            if check_key_exist.is_file():
                pass
            else:
                system("touch registeBefore")
                register_page()
        else:
            system(f"mkdir {directory}")
            chdir(f"{directory}")
            system("ls -la")
            system(f"touch registeBefore.txt")
            register_page()
            
    check()
            
except ImportError:
    print("something wrong with the modules")
            
