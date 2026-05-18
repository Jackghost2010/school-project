from random import randint
import os

###the first file


#### classes
class person:

    def __init__(self,age,name):
        self.age = age
        self.name = name


##### functions



def logins():
    while True:
        fistQuestion = input("hello mate what's your name? ")
        secondQuestion = int(input("well what's you age? "))
        user = person(secondQuestion,fistQuestion)
        print("name " + user.name + " age " + str(user.age))
        break

logins()

