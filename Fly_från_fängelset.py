### MODULES ###
import random, time, os, sys

### VARIABLES ###
Prisoner_hp = 100
prison_break = True
current_room = "meny"
Guardhp = 100
Samuraihp = 100
Chefhp = 500
loop_room_1= True
loop_room_2 = True
loop_room_3 = True
loop_room_4 = True
loop_room_5 = True

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



#Definitionen till funktionen för första rummet(Cell)
def room_1(current_room):
    while loop_room_1 == True:   
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
    while loop_room_2 == True:
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
            

        return current_room 

#Definitionen till funktionen för tredje rummet(Mini Boss)
def room_3(current_room, Prisoner_hp):
    while loop_room_3 == True:
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

            Samurai_hitchance = random.randint(1,100)
            if Samurai_hitchance >= 25:
                samuraidamage = 20
            elif Samurai_hitchance >= 50:
                samuraidamage = 40
            elif Samurai_hitchance >= 75:
                samuraidamage = 60
            elif Samurai_hitchance == 100:
                samuraidamage = 100

            Prisoner_hp = Prisoner_hp - samuraidamage
        if Prisoner_hp == 0:
            print_slow("Du är död, du får börja om ett rum tidigare.")
            current_room = "room_2"

        if Samuraihp == 0:
            print_slow("Nu är Samurai är död. ")
            print_slow("I rummet har dökt upp en dörr, vad ska du göra nu? ")
            print_slow("Fortsätt(1) eller inte(2)")
            val6 = input("Svar(1/2): ")
            if val6 == "1":
                print_slow("Du valde att fortsätta. Nu öppnar du dörren och går igenom")
                current_room = "room_4"
            elif val6 == "2":
            
                return characterweapon, current_room, ham_chance_snurr, ham_chance_sonic, katchanceaoe, katchancelightning

#Definitionen för fjärde rummet(Pusselrummet) 
def room_4(current_room):
    clear_terminal()
    riddle1_chance = 0
    riddle2_chance = 0
    riddle3_chance = 0
    while loop_room_4 == True:
            if riddle1_chance == 4 or riddle2_chance == 4 or riddle3_chance == 4:
                print_slow("Du förlora alla gåtor. Du får börja om")
                exit()
            print(riddle1_chance)
            print_slow("På väggen så finns det tre meningar, gåtor")
            print_slow("Du har tre chans varje gåta för att klara dessa gåtor, om du klarar inte så hela spelet")
            print_slow('Första gåtan är "Jag är lätt som en fjäder, men den starkaste personen kan inte hålla mig i fem minuter. Vad är jag?"')
            print_slow("Vad är ditt svar för den här gåtan")
            riddleinput1 = input("Svar: ").capitalize()
            if riddleinput1 == "Andetag":                
                print_slow('Andra gåtan är "Jag har en låda utan gångjärn, nyckel eller lock, men ändå döljer sig en gyllene skatt inuti. Vad är jag?"')
                print_slow("Vad är ditt svar")
                riddleinput2 = input("Svar: ").capitalize()
                if riddleinput2 == "Ägg":
                    print_slow('Tredje gåtan är "Jag talar utan mun och hör utan öron. Jag har ingen kropp, men jag kommer till liv med vinden. Vad är jag?"')
                    print_slow("Vad är ditt svar?")
                    riddleinput3 = input("Svar: ").capitalize()
                    if riddleinput3 == "Eko":
                        print_slow('Du svara alla gåtor rätt och nu ett dörr har dökt upp. Ovanför den står det "Chefen"')
                        print_slow("Vad vill du göra?")
                        print_slow("(1) Gå igenom dörren")
                        print_slow("(2) Gå inte igenom dörren")
                        val7 = input("Svar: ")
                        if val7 == "1":
                            print_slow("Du valde att gå igenom dörren")
                            current_room = "room_5"
                    elif riddleinput3 != "Eko" and riddle3_chance != 4:
                        riddle3_chance += 1
                        print_slow("Du klara inte tredje gåtan. Testa igen!")
                elif riddleinput2 != "Ägg" and riddle2_chance != 4:
                    riddle2_chance += 1
                    print_slow("Du klara inte andra gåtan. Testa igen!")
            elif riddleinput1 != "Andetag" and riddle1_chance != 4:
                riddle1_chance += 1
                print_slow("Du klara inte första gåtan. Testa igen!")
    return current_room

def room_5(characterweapon, ham_chance_snurr, ham_chance_sonic, katchanceaoe, katchancelightning, Prisoner_hp):
    clear_terminal()
    print_slow("I rummet så finns det en bord och stol som ryggen är mot dig.")
    print_slow('Stolen vänder mot dig, vilket sitter "Chefen". Han säger att "Jag kommer stoppa dig och att du kommer att dö.')
    print_slow('Du kommer inte äns tillbaka till din cell eller byta fängelse. Du kommer att dö."')
    print_slow("Om du klarar att döda chefen så är du FRI! Lycka till!")
    while loop_room_5 == True:
        if characterweapon == "Katana":
            print_slow("Två moves, första(1) är AOE damage baserat move, vilket ger damage i ett område för att skada fler mål.")
            print_slow("Andra(2) är att du använder elemten blixten som laddar dina katanas, du får inte lika mycket damage men högre träff chans.")
            movesinput = input("Svar 1/2: ")
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
                if characterweapon == "Big Sledge Hammer":
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

                if characterweapon == "Mjölnir":
                    mjölnir_damage_bifrost = 999
                    print_slow("Med mjölnir du kan dina motståndare till andra värld")
                if characterweapon == "MiniGun":
                    minidamage = 999
                    print_slow("Med minigun kan du skjuta och döda inom några sekunder")
        Chefhp = Chefhp - mjölnir_damage_bifrost or katdamage or hamdamage or minidamage
        if Chefhp == 0:
            print_slow("Du har dödat chefen, nu har ett dörr har dökt upp. Den är en magisk dörr som när du går igenom den ska teleportera dig till där ingen kan hitta dig.")
            print_slow("Vad vill du göra?")
            print_slow("(1) Gå igenom dörren")
            print_slow("(2) Stå kvar")
            flyktval = input("Svar: ")
            if flyktval == "1":
                print_slow("Du har valt att gå igenom dörren vilket är en smart val. Nu lever du med glädje. Nu lever du i Sydamerika")
                print_slow("Nu är du en av de rikaste personer just nu.")
                print_slow("Hejdå...")
                current_room = "finish"
            elif flyktval == "2":
                print_slow("Du har valt att stanna kvar och vakter kom. Du ")
        chef_hitchance = random.randint(1,100)
        if chef_hitchance >= 25:
            chefdamage = 15
        elif chef_hitchance >= 50:
            chefdamage = 45
        elif chef_hitchance >= 75:
            chefdamage = 80
        elif chef_hitchance == 100:
            chefdamage = 100
        Prisoner_hp = Prisoner_hp - chefdamage
        if Prisoner_hp == 0:
            print_slow("Du är död, du får börja om ett rum tidigare.")
            current_room = "room_4"
        return current_room
#Början av spelet
while (prison_break == True):
    clear_terminal()
    #menyn för spelet i loopen
    if current_room == "meny":
        current_room = meny(current_room)
    #Anropar funktionen room_1
    elif (current_room == "room_1"):
        current_room = room_1(current_room)
    #Anropar funktionen room_2
    elif (current_room == "room_2"):
        current_room = room_2(current_room)
    #Anropar funktionen room_3
    elif (current_room == "room_3"):
        current_room = room_3(current_room, Prisoner_hp)
    #Anropar funktionen room_4
    elif (current_room == "room_4"):
        current_room = room_4(current_room)
    #Anropar funktionen room_5
    elif (current_room == "room_5"):
        current_room = room_5(current_room, Prisoner_hp)
    #När spelet slutar
    else: 
        exit()