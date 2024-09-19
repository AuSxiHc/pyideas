print("Number of special characters")
n = input("Enter word: ")
count = 0
for i in range(len(n)):
    if ord(n[i]) >= 48 and ord(n[i])<= 122:
        pass
    else:
        count += 1
print(count)