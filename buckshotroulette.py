#Buckshot Roulette (Not TM) by Saisatyendra HC
#STATUS: Inactive, working on dealer ai

#ERRORS:
#1. None

#FEATURES TO ADD
#1. Dealer AI: Knows amount of rounds in shotgun (keeps shooting himself)
#2. Dealer AI: Knows his items and uses it
#3. User: Add usable items

import random as r
import time as t
import os

#Developer Menu (Can be changed)
magcap = 9 #The maximum amount of shells which can be added in the shotgun
userlife = 5
dealerlife = userlife
proceedtime = 2 #Usually 2
firetime = 1 #Usually 1

#Initializer (Do not change)
nblanks = 0 #Number of blank rounds
nlives = 0 #Number of live rounds
chance = 1 #Dealer = 0, Player = 1
inchamber = 0 #The current chambered shotgun round
roundno = 1 #Counter for the game round number
verified = 0 #Checks if the round start gun loader is fair
errstate = 0 #Error Check: Functional = 0, Bugged = 1

#User Inventory
uinv1 = None
uinv2 = None
uinv3 = None
uinv4 = None
uinv5 = None
uinv6 = None
uinv7 = None
uinv8 = None

#Dealer inventory
dinv1 = None
dinv2 = None
dinv3 = None
dinv4 = None
dinv5 = None
dinv6 = None
dinv7 = None
dinv8 = None

#Dealer Artificial Intelligence TM (Saisatyendra HC developed)
ainblanks = nblanks #Dealer assumes blanks
ainlives = nlives #Dealer assumes lives

#Prologue:
print("BUCKSHOT ROULETTE")
t.sleep(1)
print("Basic Python Adaptation by Saisatyendra HC")
t.sleep(2)
print("Starting up...")
t.sleep(1)
os.system('cls')

#Part 1: Entry...
print("Listen to all dialogue? (y/n)")
choice = input()
if choice=="y":
    t.sleep(1)
    os.system('cls')
    print("Money is tough, kid...")
    t.sleep(1)
    print("So here is the basic rundown")
    t.sleep(1)
    print("The dealer loads",magcap,"shells into the gun")
    t.sleep(1)
    print("In a random sequence...")
    t.sleep(1)
    print("Your task is to stay alive as long as possible")
    t.sleep(1)
    print("The dealer... Yes?")
    t.sleep(1)
    print("He doesnt run on those \"r.randint(0,1)\" alot anymore, or what you call them")
    input()
else:
    pass

#Part 2: The beginning rounds...
if choice=="y":
    os.system('cls')
    print("Dealer: Have a seat...")
    t.sleep(1)
    print("Dealer: Use your brain so the guy on the catwalk doesn't have to drag another body out.")
    t.sleep(2)
    print("Dealer: He gets paid, but the look on his face is a marvel.")
    t.sleep(2)
    print("Dealer: Let's begin...")
    input()
else:
    pass

#Max shells = magcap
#Empty = -1
#Live = 1
#Blank = 0
FWDloaded = []
for i in range(magcap): #Magcapacity
    FWDloaded.append(-1)
loaded = FWDloaded #Note that loaded varies, FWDloaded is permanent

while userlife!=0 and dealerlife!=0: #ROUND BEGINS
    nowload = 0
    nblanks = 0
    nlives = 0
    inchamber = 0
    ainblanks = nblanks
    ainlives = nlives
    loaded = FWDloaded
    verified = 0

    #Round Start Gun Loader V1.5 (Modified)
    while verified!=1:
        for i in range(0,magcap):
            nowload = r.randint(0,1)
            if nowload==0: #If blank
                loaded[i] = nowload
                nblanks +=1
                ainblanks += 1
            else: #If live
                loaded[i] = nowload
                nlives += 1
                ainlives += 1
        if nlives>nblanks and verified!=1:
            loaded = FWDloaded
            nblanks = 0
            nlives = 0
            ainblanks = nblanks
            ainlives = nlives
            pass
        elif (magcap - nlives)==0 and verified!=1:
            loaded = FWDloaded
            nblanks = 0
            nlives = 0
            ainblanks = nblanks
            ainlives = nlives
            pass
        elif (magcap - nblanks)==0 and verified!=1:
            loaded = FWDloaded
            nblanks = 0
            nlives = 0
            ainblanks = nblanks
            ainlives = nlives
            pass
        else:
            verified = 1

    os.system('cls')
    print("\nROUND",roundno)
    print("Dealer: ",nlives," live and ",nblanks," blank rounds are loaded in a random sequence.",sep="")
    if userlife == dealerlife:
        print("Dealer: We both have",userlife,"lives, Good luck.")
    elif userlife > dealerlife:
        print("Dealer: You have",userlife,"lives while I have only",dealerlife,"lives.")
    else:
        print("Dealer: I have",dealerlife,"lives while you have only",userlife,"lives.")
    #print("TRACE:",loaded) #Trace


    while inchamber!=magcap and userlife!=0 and dealerlife!=0:
        t.sleep(proceedtime)
        if chance==1: #Player turn
            print("\n**********")
            print("Player's turn")
            FWDuserchoice = input("Shoot (him/me): ")
            userchoice = FWDuserchoice.lower()

            if userchoice=="me": #Shoot yourself
                print("Aiming at yourself...")
                t.sleep(firetime)
                if loaded[inchamber]==1:
                    print("It was a live round")
                    print("You were shot!")
                    ainlives -= 1
                    userlife -= 1
                    inchamber += 1
                    print("You now have",userlife,"lives left")
                    chance = 0
                else:
                    ainblanks -= 1
                    print("It was a blank round")
                    print("You survived")
                    inchamber += 1

            elif userchoice=="him": #Shoot dealer
                print("Aiming at dealer...")
                t.sleep(firetime)
                if loaded[inchamber]==1:
                    print("It was a live round")
                    print("Dealer was shot!")
                    ainlives -= 1
                    dealerlife -= 1
                    inchamber += 1
                    print("Dealer now has",dealerlife,"lives left")
                    chance = 0
                else:
                    print("It was a blank round")
                    print("Dealer survived")     
                    ainblanks -= 1
                    inchamber += 1
                    chance = 0
                    
            else: #Invalid, give penalty by not chambering
                print("Invalid choice")
                print("Penalty: Giving gun to dealer")
                chance = 0
            
        else: #Dealer turn
            print("\n**********")
            print("Dealer's turn") #Skip = 0, Shoot = 1

            if inchamber==(magcap-1): #Dealer knows that the shotgun has chambered it's last round
                if ainblanks==1: #If Dealer knows it's a blank
                    dealerchoice = str(0)
                else: #If Dealer knows it's a live
                    dealerchoice = str(1)
            else: #Dealer knows that the shotgun IS NOT at it's last round
                dealerchoice = str(r.randint(0,1)) 

            if dealerchoice=="1": #Dealer shoots you
                print("Dealer aims at you...")
                t.sleep(firetime)
                if loaded[inchamber]==1:
                    print("It was a live round")
                    print("You were shot!")
                    ainlives -= 1
                    userlife -= 1
                    print("You now have",userlife,"lives left")
                    chance = 1
                else:
                    print("It was a blank round")
                    print("You survived")
                    ainblanks -= 1
                    chance = 1

            elif dealerchoice=="0": #Dealer shoots himself
                print("Dealer aims at himself...")
                t.sleep(firetime)
                if loaded[inchamber]==1:
                    print("It was a live round")
                    print("He got shot!")
                    ainlives -= 1
                    dealerlife -= 1
                    print("Dealer now has",dealerlife,"lives left")
                    chance = 1
                else:
                    print("It was a blank round")
                    print("He survived")
                    ainblanks -= 1
            else:
                print("Dealer is brain damage, you automatically win")
            inchamber += 1
    print("Dealer: Round",roundno,"is up")
    roundno += 1

print()
print("**********")
print("**********")
if userlife > dealerlife:
    print("You win!")
elif dealerlife > userlife:
    print("Dealer wins...")
else:
    print("Its a tie..?")
print("**********")
print("**********")