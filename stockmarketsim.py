#Attempted Stock Market Simulator by Saisatyendra HC
#Now lets invent stock market discrimination

import random as r #Let the stereotypes begin
import time as t
import os

#Static Factors:
maxcap = 100000 #Max Limit (def: 100k)
mincap = 1000 #Min Limit (def: 1k)
regularline = 30000 #The imaginary line which stocks stick to

#Dynamic Factors:
riselimit = 0 #Randint max limit
droplimit = 0 #Randint min limit
varyrate = 20 #Percentage allowed by randint to rise/drop
isup = -1 #If market is open (-1 undecided, 0 down, 1 up)
value = 0 #PRICE OF STOCK
prevalue = 0 #Previous record of stock value

#User Factors:
balance = 1000000 #Account of user (def: 1m)
invest = 0 #Stocks invested
status = 0 #Can open=0, Can close=1
choice = -1

#Counters:
cycles = 0 #Counter for the amount of market updates
tstocks = 0 #Total stocks bought
tsold = 0 #Total stocks sold
stupid = 0 #Amount of times the market does the stupid

os.system('cls')
print("Attempted Stock Market Simulator by Saisatyendra HC")
print("Consider this in USD")
print("You can finalize by saying \"exit\" in the buy or sell option")
print("\nPossible errors you can run into:")
print("1. \"THIS NUMBER IS TOO LARGE TO EVEN HANDLE!!!\" lol stock market profits go crazy")
print("2. \"Boolean with integer\" bla bla bla. Just restart the script and try again")
print("2. \"Cannot convert float infinity to integer\" is just the code thinking he's him")
t.sleep(1)
print("\nTip: Holding down the enter key MAY accelerate the market for your proportional gains")
t.sleep(1.5)
print("It is very much unintended for the market to give you profit. This is the result of bad coding")
isup = 1
value = regularline

t.sleep(1)
print("\nStock price: ",value)
while isup==1:
    bounceside = r.randint(0,1)
    riselimit = int(maxcap - value)
    droplimit = int(value - mincap)
    if bounceside==0: #Rise
        prevalue = value
        value+=int((varyrate/100)*riselimit)
        varyrate = r.randint(varyrate,varyrate+40)
        if varyrate<100:
            pass
        else:
            varyrate = 20
    else: #Drop
        prevalue = value
        value-=int((varyrate/100)*droplimit)
        varyrate = r.randint(varyrate-40,varyrate)
        if varyrate<100:
            pass
        else:
            varyrate = 20
    if value>(prevalue+70000): #EASTER EGG!!! This shows how stupid the code is, with all offense.
        stupid+=1
    elif value<(prevalue+70000):
        stupid+=1
    else:
        pass
    if value>0:
        print("\nStock price: ",int(value))
        print("Previous value:",prevalue)
        if status==0: #No trades, can open
            choice = input("Buy? (y/n): ")
            if choice=="y":
                choice = int(input("Enter amount of stocks to buy: "))
                if (choice*value) < balance:
                    print("Buying",choice,"stocks for",choice*value)
                    balance-=(choice*value)
                    invest+=choice
                    tstocks+=choice
                    status=1
                else:
                    print("Not enough balance")
            elif choice=="exit": #Gamblers quit 99% of the time before winning big
                print("\nClosing down the market")
                isup=0
            else:
                pass
        else: #Has active trade, can close
            choice = input("Sell? (y/n): ")
            if choice=="y":
                print("Selling",invest,"stocks for",invest*value)
                balance+=(invest*value)
                invest=0
                tsold+=invest
                status=0
            elif choice=="exit": #Gamblers quit 99% of the time before winning big
                print("\nClosing down the market")
                isup=0
            else:
                pass
    else:
        pass
    cycles+=1

os.system('cls')
print("MARKET HAS ENDED!")
print("Did you know?: \"Gamblers quit 99 percent of the time before winning big\"")
choice = input("Print bill? (y/n): ")
if choice=="y":
    print("\nTrader's bill:")
    t.sleep(2)
    print("Amount of depressing cycles gone through:",cycles)
    t.sleep(0.5)
    print("Final balance:",balance)
    t.sleep(0.5)
    print("Total stocks bought:",tstocks)
    t.sleep(0.5)
    print("Total stocks sold:",tsold)
    t.sleep(1.0)
    print("Amount of stupid things the market did (For Developers):",stupid)
else:
    print("Bro.")
    t.sleep(1)
    print("Anyways I dont really care...")
    t.sleep(1)
    print("\nTrader's bill:")
    t.sleep(2)
    print("Amount of depressing cycles gone through:",cycles)
    t.sleep(0.5)
    print("Final balance:",balance)
    t.sleep(0.5)
    print("Total stocks bought:",tstocks)
    t.sleep(0.5)
    print("Total stocks sold:",tsold)
    t.sleep(1.0)
    print("Amount of stupid things the market did (For Developers):",stupid)
print("\nThank you for playing?\n")
t.sleep(3)