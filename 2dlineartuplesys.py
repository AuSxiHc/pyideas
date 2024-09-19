x = 0
chunk = [1,0,0,0,0]
pos = -1

print(chunk,"X Position=",x)
while pos!="exit":
    pos = input()
    if pos=="d": #Right
        chunk[x] = 0
        x+=1
        chunk[x] = 1
    elif pos=="a": #Left
        chunk[x] = 0
        x-=1
        chunk[x] = 1
    else: #Invalid Input
        pass
    print(chunk,"X Position=",x)