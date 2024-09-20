#Attempted Stock Market Simulator by Saisatyendra HC
#Now lets invent stock market discrimination

import random as r #Let the stereotypes begin
import time as t

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

print("#Attempted Stock Market Simulator by Saisatyendra HC")
isup = 1
value = regularline

t.sleep(1)
print("\nStock price: ",value)
while isup==1:
    bounceside = r.randint(0,1)
    riselimit = int(maxcap - value)
    droplimit = int(value - mincap)
    if bounceside==0: #Rise
        value+=(varyrate/100)*riselimit
        varyrate = r.randint(varyrate,varyrate+40)
        if varyrate<100:
            pass
        else:
            varyrate = 20
    else: #Drop
        value-=(varyrate/100)*droplimit
        varyrate = r.randint(varyrate-40,varyrate)
        if varyrate<100:
            pass
        else:
            varyrate = 20
    if value>0:
        print("\nStock price: ",int(value))
        t.sleep(1)
    else:
        pass