import math as m

direc = None
x = 0
y = 1
chunk = 10 #Square Dimensions of Chunk

#New Launch Render Engine
print("Coordinates: (",x,",",y,")",sep="")

while direc!="exit":
    direc = input("Enter Direction: ")
    if direc=="w":
        if (y+1)<chunk:
            y+=1
        elif (y+1)<0:
            print("Error, Chunk Boundary")
        else:
            print("Error, Chunk Boundary")
    elif direc=="a":
        if (x-1)<chunk:
            x-=1
        elif (x-1)<0:
            print("Error, Chunk Boundary")
        else:
            print("Error, Chunk Boundary")
    elif direc=="s":
        if (y-1)<chunk:
            y-=1
        elif (y-1)<0:
            print("Error, Chunk Boundary")
        else:
            print("Error, Chunk Boundary")
    elif direc=="d":
        if (x+1)<chunk:
            x+=1
        elif (x+1)<0:
            print("Error, Chunk Boundary")
        else:
            print("Error, Chunk Boundary")
    else:
        pass

    #Active Render Engine
    print("\n\n\n\n")
    for j in range(0,chunk):
        if j==y:
            for i in range(0,chunk):
                if i==x:
                    print("I",sep="",end="")
                else:
                    print(" ",sep="",end="")
        else:
            for i in range(0,chunk):
                print(" ",sep="",end="")
        print()
    print("Coordinates: (",x,",",y,")",sep="")