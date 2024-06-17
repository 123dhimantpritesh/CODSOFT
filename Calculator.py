print('''welcome to calculator !! \nEnter the two numbers respectively''')
a = int(input("Please Enter the first Number ! "))
b = int(input("Please Enter the second Number ! "))
c = int(input('''Select the operation you want to perform by enter the no. of operation :
                        1. ADDITION
                        2. SUBSTRACTION
                        3. MULTIPLICATION
                        4. DIVISION
                        5. Exit \n'''))
if c == 1 :
    print("The sum of two numbers is : ", a + b)
elif c == 2:
    print("The difference of two numbers is : ", a - b)
elif c == 3:
    print("The product of two numbers is : ", a * b)
elif c == 4:
    print("The quotient is : ", float(a/b))
elif c == 5:
    print('''Exiting the calculator
          Thanks for using !''')
else:
    print("Invalid operation selected !")