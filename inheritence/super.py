class employee:
    def __init__(self):
        print("constructor of employee")
    a=1  
 
class programmer(employee):
    def __init__(self):
        print("constructor of programer")
    b=2
    
class manager(programmer):
    def __init__(self):
        super().__init__()       # this will aadd the constructor of parent class also
        print("constructor of manager")
    c=3
    
# o=employee()
# print(o.a)  # prints the attributes of a

# o=programmer()
# print(o.a,o.b)  

o=manager()
print(o.a,o.b,o.c)