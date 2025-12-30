# write a recursive function to print sum of first n natural numbers

def natural(n):
    if(n==1):
        return 1
    return natural(n-1)+ n
    
n=int(input("enter the number"))
a=natural(n)
print(a)