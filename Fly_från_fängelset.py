### MODULES ###
import random, time, os, sys

### VARIABLES ###
Prisoner_hp = 100
Prisoner_hitchance = random.randint(7,10)
prison_break = True
current_room = "room_1"
guardhp = 100
Samuraihp = 100

### FUNCTIONS ###

#För att skriva sakta bokstav för bokstav
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
        "\ndu har en ventilationsgaller bredvid dig som "
        "\ngår till fängelsets ventilation, vill du öppna den med skruvmejsel "
        "\ndu har?")
    val2 = input("Ja/Nej? ").lower()
    if (val2 == "ja"):
        current_room = "room_2"
    
    elif (val2 == "nej"):
        print("Du vill stanna kvar här")
        print("Till slut dör du av svält. Game over.")
        exit()
    return current_room

def room_2(current_room):
    clear_terminal()
    print_slow("Nu är du i ventilation")
    print_slow("Du har två väg, höger eller vänster")
    print_slow("1. Höger"
    "\n2. Vänster")
    val3 = input("Svar (1/2)")
    if val3 == "1":
        try:
            print_slow("Du går höger i ventilationen")
            print_slow("Vid den sida sover vakt. Du kan döda han med kniv")
            print_slow("Vill du eller inte?")
            val4 =input("Svar(Ja/Nej)? ").lower()
            if (val4 == "ja"):
                träffchans = random.randint(1,10)
                if träffchans >= 4:
                    guardhp = guardhp - 100
                    print_slow("Vakten är död och du hittat en kort, nu fortsätter du genom koridoren och slutet av koridoren så finns det en dör med kortläsare du öppnar dörren och går igenom. ")
                
                elif val4 == "Ja":
                    current_room = "room_3"
                
                else:
                    prison_break = False
        except:
            return current_room, prison_break, guardhp

def room_3():
    clear_terminal()
    print_slow("Nu är du i en stor rum, det är knivar i vägen, det finns blod på de. ")
    print_slow("Andra sidan av rummet är det en Samurai med två svärd. ")
    print_slow("Du får välja dina vapen")
    input("")


    

#Början av spelet
while (prison_break == True):
    if (current_room == "room_1"):
        #Anropar funktionen room_1
        current_room = room_1(current_room)
    elif (current_room == "room_2"):
        #Anropar funktionen room_2
        current_room = room_2(current_room)
    else: 
        exit()