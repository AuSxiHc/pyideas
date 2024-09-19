#Minecraft 2D by Saisatyendra HC
#My rights are undeserved.

#Player Coordinates:
x = 0 #Horizontal
y = 1 #Vertical (Player above blocks)

#The World: ()
y5base = [0,0,0,0,0]
y4base = [0,0,0,0,0]
y3base = [0,0,0,0,0]
y2base = [0,0,0,0,0]
y1base = [0,0,0,0,0]
y0base = [1,1,1,1,1]

#0 = Air, 1 = Block

#Convert world data into GUI:
for y5 in range(4): #On layer 5
    if y5base[y5] == 0:
        print(" ",sep="",end="")
    elif y5base[y5] == 1:
        print("#",sep="",end="")
print()
for y4 in range(4): #On layer 4
    if y4base[y4] == 0:
        print(" ",sep="",end="")
    elif y4base[y4] == 1:
        print("#",sep="",end="")
print()
for y3 in range(4): #On layer 3
    if y3base[y3] == 0:
        print(" ",sep="",end="")
    elif y3base[y3] == 1:
        print("#",sep="",end="")
print()
for y2 in range(4): #On layer 2
    if y2base[y2] == 0:
        print(" ",sep="",end="")
    elif y2base[y2] == 1:
        print("#",sep="",end="")
print()
for y1 in range(4): #On layer 1
    if y1base[y1] == 0:
        print(" ",sep="",end="")
    elif y1base[y1] == 1:
        print("#",sep="",end="")
print()
for y0 in range(4): #On layer 0
    if y0base[y0] == 0:
        print(" ",sep="",end="")
    elif y0base[y0] == 1:
        print("#",sep="",end="")
print()