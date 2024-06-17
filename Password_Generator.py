import string
import random

length= int(input("Enter the Length of password : "))
print ('''choose character set for password from these :
       1. Digits
       2. Letters
       3. Special Characters
       4. Exit ''')
cl=""
while(True):
    c=int(input("pick a number "))
    if (c==2):
        cl+=string.ascii_letters
    elif(c==1):
        cl+=string.digits
    elif(c==3):
        cl+=string.punctuation
    elif(c==4):
        break
    else:
        print("please choose a valid option ! ")
Pass= []
for i in range(length):
    randchar=random.choice(cl)
    Pass.append(randchar)
print("The random password is " + "".join(Pass))   