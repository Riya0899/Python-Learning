# write a class "calculator" capable of finding square,cube and square root of a number

class calculator:
    def __init__(self,n):
        self.n=n
        
    def square(self):
        print(f"the square is {self.n*self.n}")
        
    def cube(self):
        print(f"the cube is {self.n*self.n*self.n}")
       
    def sqrt(self):
        print(f"the squareRoot is {self.n**1/2}")

n=int(input("enter the number"))
a=calculator(n)
a.square()
a.cube()
a.sqrt()