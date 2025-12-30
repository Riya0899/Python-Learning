# a=int(input("enter your number:"))
# b=int(input("enter your number:"))
# c=int(input("enter your number:"))

# average=(a+b+c)/3

# print(average)

# for 50 users line of code is too much so thats why for this repeteetion we use functions

def avg():           # function definition
    a=int(input("enter your number:"))
    b=int(input("enter your number:"))
    c=int(input("enter your number:"))

    average=(a+b+c)/3

    print(average)
    
avg()
avg()
avg()   # function calling

def greet(): 

    user=input("enter the name of the user")
    print("good morning",user)
    
greet()