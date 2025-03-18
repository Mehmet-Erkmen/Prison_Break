#MODULES
import random, time, os, sys

#VARIABLES
Prisoner_hp = 100
Prisoner_hitchance = random.randint(7,10)
prison_break = True
current_room = "room_1"

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

def room_1(current_room):
    print_slow("Du är i en cell, som är tom")
    print_slow("1. Söka rummet")
    print_slow("2. Försök öppna dörren")
    print_slow("Vad vill du göra?")
    val1 = input(""
    "\nSvar (1/2): ")
    if (val1 == "1"):
        print_slow("Nu söks rummet...")
        time.sleep(2)
        print_slow("Du har hittat en kniv och skruvmejsel"
        "\n du har en ventilationsgaller bredvid dig som "
        "\n går till fängelsets ventilation, vill du öppna den med skruvmejsel "
        "\n du har?")
    val2 = input("Ja/Nej? ").lower
    if val2 == "ja":
        current_room = "room_2"
    return current_room

def room_2(current_room):
    clear_terminal()
    print_slow("Nu är du i ventilation")


    

#test_function

#Början av spelet
while (prison_break == True):
    if (current_room == "room_1"):
        current_room = room_1(current_room)
    elif (current_room == "room_2"):
        current_room = room_2(current_room)
    else: 
        exit()
    