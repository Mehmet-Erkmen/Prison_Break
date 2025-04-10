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

#För att skriva sakta bokstav för bokstav till menyn
def print_slow_meny(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.009)
    sys.stdout.write("\n")
    sys.stdout.flush()
def meny():
    print_slow_meny("""
__________        .__                        __________                        __    
\______   \_______|__| __________   ____     \______   \_______   ____ _____  |  | __
 |     ___/\_  __ \  |/  ___/  _ \ /    \     |    |  _/\_  __ \_/ __ \\__  \ |  |/ /
 |    |     |  | \/  |\___ (  <_> )   |  \    |    |   \ |  | \/\  ___/ / __ \|    < 
 |____|     |__|  |__/____  >____/|___|  /    |______  / |__|    \___  >____  /__|_ \\
                          \/           \/            \/              \/     \/     \/ 
""")
    print_slow("1. Börja med spelen")
    print_slow("2. Sluta")
    valmeny = input("Svar(1/2): ")
    if valmeny == "2":
        exit()

#Funktion för att skriva text sakta bokstav för bokstav
def print_slow(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.04)
    sys.stdout.write("\n")
    sys.stdout.flush()
#För att rensa tidigare text.
def clear_terminal():
    if os.name == 'nt':
        os.system('cls')



#Definitionen till funktionen för första rummet
def room_1(current_room):
    clear_terminal()
    print_slow("Du är i en cell, som är tom")
    print_slow("1. Söka rummet")
    print_slow("2. Försök öppna dörren")
    print_slow("Vad vill du göra?")
    val1 = input(""
    "\nSvar (1/2): ")
    if (val1 == "1"):
        print_slow("Nu söks rummet...")
        time.sleep(2)
        print_slow("Du har hittat en kniv och skruvmejsel")
        print_slow("Vad vill du göra?")
        print_slow("1. Öppna ventilation")
        print_slow("2. Stanna kvar.")
        val2 = input("Svar(1/2): ").lower()
        if (val2 == "1"):
            current_room = "room_2"

    
        elif (val2 == "2"):
            print("Du vill stanna kvar här")
            print("Till slut dör du av svält. Game over.")
            exit()
    elif (val1 == "2"):
        print_slow("Dörren är låst. ")
    return current_room

#Definitionen till funktionen för andra rummet
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
            print_slow("Vid den sida sover vakt.")
            print_slow("Vad vill du göra?")
            print_slow("1. Döda han.")
            print_slow("2. Gå förbi han(han kan vakna)")
            val4 =input("Svar(1/2)? ").lower()
            if (val4 == "1"):
                träffchans = random.randint(1,10)
                if träffchans >= 4:
                    guardhp = guardhp - 100
                    print_slow("Vakten är död och du hittat en kort, nu fortsätter du genom koridoren och slutet av koridoren så finns det en dör med kortläsare du öppnar dörren och går igenom. ")
                
                elif val4 == "2":
                    wakeupchance = random.randint(1,10)
                    if wakeupchance >=7:
                        print_slow("Han vakna inte, du fortsätter") 
                        current_room = "room_3"
                
                else:
                    prison_break = False
        except:
            return current_room, prison_break, guardhp

#Definitionen till funktionen för tredje rummet
def room_3(current_room):
    clear_terminal()
    print_slow("Nu är du i en stor rum, det är knivar i vägen, det finns blod på de. ")
    print_slow("Andra sidan av rummet är det en Samurai med två katana, en stor en små. ")
    print_slow("Du får välja dina vapen")
    print_slow("Katana(1)")
    print_slow("Big Sledge Hammer(2)")
    weaponinput = input("Svar(1/2)")
    if weaponinput == "1":
        characterweapon = "Katana"
        katchance = random.randint(1,100)
        if katchance < 25:
            katdamage = 0
        elif katchance >=25:
            katdamage = 10
        elif katchance >= 50:
            katdamage = 20
        elif katchance >= 75:
            katdamage = 30
        elif katchance == 100:
            katdamage = 100
    elif weaponinput == "2":
        characterweapon = "Two-Handed Hammer"
        hamchance = random.randint(1,100)
        if hamchance >=25:
            hamdamage = 15
        elif hamchance >= 50:
            hamdamage = 30
        elif hamchance >= 75:
            hamdamage = 45
        elif hamchance == 100:
            hamdamage = 100

    elif weaponinput == "Ragnarök":
        characterweapon = "Mjölnir"
    elif weaponinput == "Nuttertools":
        characterweapon == "MiniGun"
    
    if Samuraihp == 0:
        current_room = "room_4"
    
    return characterweapon, current_room


    

#Början av spelet
while (prison_break == True):

    clear_terminal()
    meny()

    #Anropar funktionen room_1
    if (current_room == "room_1"):
        current_room = room_1(current_room)

    #Anropar funktionen room_2
    elif (current_room == "room_2"):
        current_room = room_2(current_room)

    #Anropar funktionen room_3
    elif (current_room == "room_3"):
        current_room = room_3(current_room)
    else: 
        exit()