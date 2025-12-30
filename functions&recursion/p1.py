def greatest():
    if(num1>num2 and num1>num3):
        print(f"{num1} is greatest")
    elif(num2>num1 and num2>num3):
         print(f"{num2} is greatest")
    elif(num3>num1 and num3>num2):
         print(f"{num3} is greatest")   
    else:
        print("enter valid number")
num1=int(input("enter number1"))       
num2=int(input("enter number2"))       
num3=int(input("enter number3"))       
greatest()