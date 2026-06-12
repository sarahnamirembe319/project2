#simple basic calculator
print("----menu---")
print("multiplication---1")
print("addition---------2")
print("subtraction------3")
print("division---------4")
print("quit-------------5")
value=int(input("enter your choice;"))
if value==5:
    print("goodbye")
    


elif value==1:
    num1=int(input("enter first number:\n"))
    num2=int(input(" enter second number:\n"))
    print (f"{num1}*{num2}=",num1*num2)
elif value==2:
    num1=int(input("enter first number:\n"))
    num2=int(input(" enter second number:\n"))
    print(f"{num1}+{num2}=",num1+num2)
elif value==3:
    num1=int(input("enter first number:\n"))
    num2=int(input(" enter second number:\n"))
    print(f"{num1}-{num2}=",num1-num2)
elif value==4:
    while True:
        num1=int(input("enter first number:\n"))
        num2=int(input(" enter second number:\n"))
        if num2==0:
            print("the divisor can not be zero (0)")
        else:
            print(f"{num1}/{num2}={num1/num2:.2f} to 2decimals")
            break
else:
    print("please enter a valid number on the menu")
