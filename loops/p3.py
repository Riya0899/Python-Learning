#wap to find whether a given number is prime or not

num=int(input("enter a number"))
for i in range(2,num):
    if(num%i)==0:
        print("not prime")
        break
else:
    print("prime")    