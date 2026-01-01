a=int(input("enter number one"))
b=int(input("enter number second"))

if(b==0):
    raise ZeroDivisionError("hey our program is not meant for divide numbers by zero")
else:
    print(f"the division a/b is {a/b}")
    