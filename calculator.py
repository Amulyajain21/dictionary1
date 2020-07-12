from math import *
#function add
def add(x,y):
    return x+y
#function subtract
def subtract(x,y):
    return x-y
#function multiply
def multiply(x,y):
    return x*y
#function divide
def divide(x,y):
    return x/y
#function squart
print("what we want to use")
print(" 1. general calculator")
print(" 2. scientific calculator")
choice = input("enter choice")
if choice == '1':
  while choice2=='y':
    print("you choose general calculator for calculation")
    print("1. Addition")
    print("2. Subtraction ")
    print("3. Multiplication")
    print("4. division")
    ch = input("enter choice")
    num1 = int(input("enter first number"))
    num2 = int(input("enter second number"))
    choice2 ='y'
    if ch == '1':
        print(num1,"+",num2,"=", add(num1,num2))
        choice2=input("do you want to repeat")
    elif ch == '2':
        print(num1,"-",num2,"=", subtract(num1,num2))
        choice2=input("do you want to repeat")
    elif ch == '3':
        print(num1,"*",num2,"=", multiply(num1,num2))
        choice2=input("do you want to repeat")
    elif ch == '4':
        print(num1,"/",num2,"=", divide(num1,num2))
        choice2=input("do you want to repeat")
    else :
        print("invalid enter")
elif choice == '2':
    choice2 ='y'
    while choice2 == 'y':
     from math import *
     print("you choose general calculator for calculation")
     print("1. Addition")
     print("2. Subtraction ")
     print("3. Multiplication")
     print("4. division")
     print("5. power")
     print("6. log")
     print("7. sin")
     print("8. cos")
     print("9. tan")
     print("10. tanh")
     print("11. sinh")
     print("12. cosh")
     print("13. square root")
     print("14. radians")
     print("15. degree")
     ch = input("enter choices")
     
     if ch == '1':
        num1 = int(input("enter num 1"))
        num2 = int(input("enter num 2"))
        print(num1,"+",num2,"=", add(num1,num2))
        choice2=input("do you want to repeat")
        
     elif ch == '2':
        num1 = int(input("enter num 1"))
        num2 = int(input("enter num 2"))
        print(num1,"-",num2,"=", subtract(num1,num2))
        choice2=input("do you want to repeat")
     elif ch == '3':
        num1 = int(input("enter num 1"))
        num2 = int(input("enter num 2"))
        print(num1,"*",num2,"=", multiply(num1,num2))
        choice2=input("do you want to repeat")
     elif ch == '4':
        num1 = int(input("enter num 1"))
        num2 = int(input("enter num 2"))
        print(num1,"/",num2,"=", divide(num1,num2))
        choice2=input("do you want to repeat")
     elif ch == '5':
        num1 = int(input("enter num 1"))
        num2 = int(input("enter num 2"))
        print(pow(num1,num2))
        choice2=input("do you want to repeat")
     elif ch == '6':
        num= int(input("enter the no."))
        print(log(num))
        choice2=input("do you want to repeat")
     elif ch == '7':
        num = int(input("enter the no."))
        print(sin(num))
        choice2=input("do you want to repeat")
     elif ch == '8':
        num = int(input("enter the no."))
        print(cos(num))
     elif ch == '9':
        num = int(input("enter the no."))
        print(tan(num))
     elif ch == '10':
        num = int(input("enter the no."))
        print(tanh(num))
     elif ch == '11':
        num = int(input("enter the no."))
        print(sinh(num))
     elif ch == '12':
        num = int(input("enter the no."))
        print(cosh(num))
     elif ch == '13':
        num = int(input("enter the no."))
        print(sqrt(num))
     elif ch == '14':
        num = int(input("enter the no."))
        print(radians(num))
     elif ch == '15':
        num = int(input("enter the no."))
        print(degrees(num))
        
else :
    print("invalid input")
    
    
    
       
   
    
    

