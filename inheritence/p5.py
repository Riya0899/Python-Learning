class vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
        
    def __add__(self,other):
        result=vector(self.x+other.x,self.y+other.y,self.z+other.z)
        return result
    
    def __mul__(self,other):
        result=vector(self.x*other.x,self.y*other.y,self.z*other.z)
        return result
    
    def __str__(self):
        return f"vector({self.x},{self.y},{self.z})"

v1=vector(1,2,3)
v2=vector(11,21,13)
v3=vector(16,25,33)

print(v1+v2)
print(v1*v2)


print(v1+v3)
print(v1*v3)


