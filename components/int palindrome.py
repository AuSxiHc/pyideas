num = int(input("Enter number: "))
temp = num
reverse = 0
remainder = None
print("**********")
while temp > 0:
    remainder = temp % 10
    reverse = (reverse * 10) + remainder
    temp = temp // 10
print("Reverse",reverse)