# create a class "programmer" for storing information of few programmers working at microsoft

class programmer:
    company="microsoft"
    
    def __init__(self,name,salary,address):
        self.name=name
        self.salary=salary
        self.address=address
        
p=programmer("riya",120000,"chandigarh")
print(p.name,p.address,p.salary)      
                
r=programmer("rohan",120000,"ludhiana")
print(r.name,r.address,r.salary)   
                
s=programmer("sohan",140000,"ludhiana")
print(s.name,s.address,s.salary)        
                
    
    