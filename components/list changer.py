#Edit List

list = [0,0,0,0,0]

print("Given list:")
print(list,"\n")

setname = int(input("What set to change: "))
print("Set to change:",setname,"\n")
setname = setname - 1

setno = int(input("What to change in the set: "))
print("Set to change:",setno,"\n")

list[setname] = setno

print("New Dictionary:",list)
