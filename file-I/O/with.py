f=open("file.txt")  
data=f.read()
print(data)
f.close()

# the same can be written using with statement

with open("file.txt") as f:
    print(f.read())
    
    # you dont have to explicitly close the file