### MODULES ###
import random, time, os, sys

### VARIABLES ###
Prisoner_hp = 100
Prisoner_hitchance = random.randint(7,10)
prison_break = True
current_room = "meny"
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
def meny(current_room):
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
    if valmeny == "1":
        current_room = "room_1"
    elif valmeny == "2":
        exit()
    return current_room

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



#Definitionen till funktionen för första rummet(Cellen)
def room_1(current_room):
    clear_terminal()
    print_slow("Du är i en cell, som är tom")
    print_slow("1. Söka rummet")
    print_slow("2. Försök öppna dörren")
    print_slow("Vad vill du göra?")
    val1 = input("Svar (1/2): ")
    if (val1 == "1"):
        print_slow("Nu söks rummet...")
        time.sleep(2)
        print_slow("Du har hittat en kniv och skruvmejsel")
        print_slow("Vad vill du göra?")
        print_slow("1. Öppna ventilation")
        print_slow("2. Stanna kvar.")
        val2 = input("Svar(1/2): ")
        if (val2 == "1"):
            current_room = "room_2"
        elif (val2 == "2"):
            print("Du vill stanna kvar här")
            print("Till slut dör du av svält. Game over.")
            exit()
    elif (val1 == "2"):
        print_slow("Dörren är låst. ")
    return current_room

#Definitionen till funktionen för andra rummet(Ventilation)
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
        
    if val3 == "2":
        print_slow("Du är sluttet av ventilation och i korridoren så finns det en dörr")
        print_slow("Vad ska du göra? ")
        print_slow("Öppna dörren(1)")
        print_slow("Stanna kvar(2)")
        val5 = input("Svar: (1/2): ")
        if val5 == "1":
            current_room = "room_3"
        

    return current_room, prison_break, guardhp

#Definitionen till funktionen för tredje rummet(Mini Boss)
def room_3(current_room):
    clear_terminal()
    print_slow("Nu är du i en stor rum, det är olika vapen i vägen, det finns blod på de. ")
    print_slow("Andra sidan av rummet är det en Samurai med två katana, en stor och en små. ")
    print_slow("Hela rummet är gjord av oförstörbar metal.")
    print_slow("Du får välja dina vapen")
    print_slow("Katana(1)")
    print_slow("Två moves, första(1) är AOE damage baserat move, vilket ger damage i ett område för att skada fler mål.")
    print_slow("Andra(2) är att du använder elemten blixten som laddar dina katanas, du får inte lika mycket damage men högre träff chans.")
    print_slow("Big Sledge Hammer(2)")
    print_slow("(1)För denna vapen är det så att du snurrar med din hammer och får låg träff chans men hög damage.Det var första move.")
    print_slow("(2)Du kan också slå hammaren på marken för att hela rummen gjord av oförstörbar metal, vilket kommer skapa en sonisk våg.")
    weaponinput = input("Svar(1/2)")

    print_slow(f"Du har valt{weaponinput} nu du får slåss mot Samurai")
    print_slow("Välj dina moves")
    if characterweapon == "Katana":
        print_slow("Två moves, första(1) är AOE damage baserat move, vilket ger damage i ett område för att skada fler mål.")
        print_slow("Andra(2) är att du använder elemten blixten som laddar dina katanas, du får inte lika mycket damage men högre träff chans.")
        movesinput = input("Svar 1/2: ")
        if weaponinput == "1":
            characterweapon = "Katana"
            katchancelightning = random.randint(1,100)
            katchanceaoe = random.randint(1,100)
            #Katanas med laddad blixt
            if movesinput == "1":
                if katchancelightning < 25:
                    katdamage = 0
                elif katchancelightning >=25:
                    katdamage = 10
                elif katchancelightning >= 50:
                    katdamage = 20
                elif katchancelightning >= 75:
                    katdamage = 30
                elif katchancelightning == 100:
                    katdamage = 100
            #Katanas med AOE
            if movesinput == "2":
                if katchanceaoe < 25:
                    katdamage = 0
                elif katchanceaoe >=25:
                    katdamage = 5
                elif katchanceaoe >= 50:
                    katdamage = 10
                elif katchanceaoe >= 75:
                    katdamage = 15
                elif katchanceaoe == 100:
                    katdamage = 20
        elif weaponinput == "2":
            characterweapon = "Big Sledge Hammer"
            ham_chance_sonic = random.randint(1,100)
            ham_chance_snurr = random.randint(1,100)
            if ham_chance_snurr >=25:
                hamdamage = 10
            elif ham_chance_snurr >= 50:
                hamdamage = 30
            elif ham_chance_snurr >= 75:
                hamdamage = 55
            elif ham_chance_snurr == 100:
                hamdamage = 70
            if ham_chance_sonic >=25:
                hamdamage = 10
            elif ham_chance_sonic >= 50:
                hamdamage = 30
            elif ham_chance_sonic >= 75:
                hamdamage = 55
            elif ham_chance_sonic == 100:
                hamdamage = 70

        elif weaponinput == "Ragnarök":
            characterweapon = "Mjölnir"
            mjölnir_damage_bifrost = 999
            print_slow("Med mjölnir du kan dina motståndare till andra värld")
        elif weaponinput == "Nuttertools":
            characterweapon == "MiniGun"
            minidamage = 999
            print_slow("Med minigun kan du skjuta och döda inom några sekunder")

        Samuraihp = Samuraihp - hamdamage or katdamage or mjölnir_damage_bifrost or minidamage
        
    if Samuraihp == 0:
        print_slow("Nu är Samurai är död. ")
        print_slow("I rummet har dökt upp en dörr, vad ska du göra nu? ")
        print_slow("Fortsätt(1) eller inte(2)")
        val6 = input("Svar(1/2): ")
        if val6 == "1":
            print_slow("Du valde att fortsätta. Nu öppnar du dörren och går igenom")
            current_room = "room_4"
        elif val6 == "2":
        
            return characterweapon, current_room, hamdamage, ham_chance_snurr, ham_chance_sonic, katchanceaoe, katchancelightning, katdamage, mjölnir_damage_bifrost, minidamage

#Definitionen för fjärde rummet(Pusselrummet) 
def room_4():
    print_slow("På väggen så finns det tre meningar, gåtor")
    print_slow('Vilket står "Jag är lätt som en fjäder, men den starkaste personen kan inte hålla mig i fem minuter. Vad är jag?"')
    print_slow("Vad är ditt svar för den här gåtan")
    riddleinput1 = input("Svar: ").lower
    if riddleinput1 == "Andetag":
        print_slow('Andra gåtan är "Jag har en låda utan gångjärn, nyckel eller lock, men ändå döljer sig en gyllene skatt inuti. Vad är jag?"')
        print_slow("Vad är ditt svar")
#Början av spelet
while (prison_break == True):
    room_4()
    clear_terminal()
    #menyn för spelet i loopen
    if current_room == "meny":
        current_room = meny(current_room)
    #Anropar funktionen room_1
    if (current_room == "room_1"):
        current_room = room_1(current_room)
    #Anropar funktionen room_2
    elif (current_room == "room_2"):
        current_room = room_2(current_room)
    #Anropar funktionen room_3
    elif (current_room == "room_3"):
        current_room = room_3(current_room)
    #När spelet slutar
    else: 
        exit()