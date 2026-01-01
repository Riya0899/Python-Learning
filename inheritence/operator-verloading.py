class number:
    def __init__(self,n):
        self.n = n
        
    def __add__(self,num):
        return self.n+num.n   # define the add method
    
    
n=number(2)
m=number(3)

print(n+m)

# some other dunder methods are
 
# def __sub__()
# def __mul__()
# def __str__()
# def __len__()
# def __truediv__()
# def __floordiv__()