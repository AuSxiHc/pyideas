#Queue Sytem
queue = []
choice = None
sys = 1

while sys==1:
    print("\nQUEUE SYSTEM")
    print("1. Append new value to queue")
    print("2. Extract a value and process")
    print("3. View queue")
    choice = input("Enter choice: ")
    if choice=="1":
        choice = input("\nEnter new value: ")
        queue.append(choice)
    elif choice=="2":
        print("\n",queue[0])
        for i in range(len(queue)):
            if i!=(len(queue)-1):
                queue[i]=queue[i+1]
            else:
                pass
        queue.pop(len(queue)-1)
    elif choice=="3":
        print("\n",queue)
    else:
        print("\nInvalid choice!")