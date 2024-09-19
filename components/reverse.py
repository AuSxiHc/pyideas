print("Reverse of String")
n = input("Enter string: ")
rsv = 0
for i in range(len(n)):
    if rsv == 0:
        rsv = n[(len(n)-1) - i]
    else:
        rsv = rsv + n[(len(n)-1) - i]
print(rsv)