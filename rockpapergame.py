from operator import truediv
import random
from secrets import choice
from sys import path_importer_cache
available_options = ['R', 'P', 'S']
R="Rock"
P="paper"
S="scissors"
R>S
P>R
S>P
not_playing=False 
while not_playing is False:
    asking = True
    while asking is True:
        print("welcome to RSP game")
        user_option= input("choose an option: R, P, or S" "\n")
        if user_option == "P":
            print("your option is:  ", P)
        asking = False  
        if user_option == "R":
            print("your option is:  ", R)
        asking = False
        if user_option == "S":
            print("your option is:  ", S)
        asking = False
        if not user_option in available_options:
            print("not in our options")
            asking=True

    computer_option = random.choice(available_options)
    if computer_option=="R":
        print("compuer option is:  ", R)
    if computer_option=="P":
        print("compuer option is:  ",P)
    if computer_option=="S":
        print("compuer option is:  ",S)
    if computer_option > user_option:
        print("computer win")
        not_playing=True
    if user_option > computer_option:
        print("congratulations, you win")
        not_playing=True
    if user_option==computer_option:
        pass 