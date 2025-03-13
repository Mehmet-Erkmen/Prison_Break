#MODULES
import random, time, os, sys

#VARIABLES
Prisoner_hp = 100
Prisoner_hitchance = random.randint(7,10)

#FUNCTIONS

def print_slow(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.04)
    sys.stdout.write("\n")
    sys.stdout.flush()
def clear_terminal():
    if os.name == 'nt':
        os.system('cls')

def room_1():
    print_slow("Du är i en cell, som är tom")
    print_slow("1. Söka rummet")
    print_slow("2. Försök öppna dörren")
    val1 = input("Vad vill du göra?"
    "\nSvar (1/2): ")
    if (val1 == "1"):
        print_slow("Nu söks rummet...")
        time.sleep(2)
        print_slow("Du har hittat en nyckel")

#test_function
room_1()

#Början av spelet


