#WAP to find the greatest of 3 numbers entered by the user

num1= int(input("enter num1: "))
num2= int(input("enter num1: "))
num3= int(input("enter num1: "))

if (num1 >= num2) and (num1 >= num3):
    print("num1 is the greatest.")
elif (num2 >= num1) and (num2 >= num3):
    print("num2 is the greatest.")
else:
    print("num3 is the greatest.")