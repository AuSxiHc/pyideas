#Cross Terminal Communicator
#By Saisatyendra HC

#SYSTEM 1

#1. Find comms file in same directly
#2. System data is stored there
#3. Use batch

import os
import time as t

#Clear terminal
os.system('cls')

#Initialze
path = os.getcwd()
direc = os.open(path, os.O_RDONLY) 

#Developer Variables:
bitrate = 2

readBytes = os.read(direc, bitrate) 
  
# Print the bytes read 
print(readBytes) 
  
# close the file descriptor 
os.close(direc) 