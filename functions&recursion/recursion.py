# function calling itself is recursion 
'''
factorial(0)= 1
factorial(1)= 1
factorial(2)= 2 x 1
factorial(3)= 3 x 2 x 1
factorial(4)= 4 x 3 x 2 x 1
factorial(5)= 5 x 4 x 3 x 2 x 1
factorial(n)= n*factorial(n-1)
'''

def factorial(n):
    if(n==0 or n==1):
        return 1
    return n*factorial(n-1)

n=int(input("enter the number"))
print(f"factorial of given number is {factorial(n)}")

#using for loop

def factorial(n):
    result=1
    for i in range(1,n+1):
        result*=i
    return result
        
for num in range(1,6):
    print(f"{num}!={factorial(num)}")  

# using for loop to find fact of one number

n=int(input("enter the number you want the factorial of"))
factorial=1
if(n==0 or n==1):
    print("factorial is 1")
else:
    for i in range(1,n+1):
        factorial*=i
    print(f"factorial of this number is {factorial}")
        