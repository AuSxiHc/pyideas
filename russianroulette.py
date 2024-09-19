import random as r
round = -1
while round!=6:
    rand = r.randint(1,7)
    if rand!=6:
        print("Survival",rand)
        input()
    else:
        print("Dead",rand)
        break