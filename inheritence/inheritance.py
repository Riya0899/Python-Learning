class employee:
    company="ITC"
    
    def show(self):
        print(f"the name of the employee is {f.name} and salary is {self.salary}")
        
# class programmer:
#     company="ITC infotech"
    
#     def show(self):
#         print(f"the name of the employee is {f.name} and salary is {self.salary}")
        
#     def showlanguage(self):
#         print(f"the name of the employee is {f.name} and is good with  {self.language}")


# INSTEAD OF DOING COPY PASTE OF ONE CLASS CODE TO OTHER WE USE THE CONCEPT OF INHERITENCE

class programmer(employee):
    company="ITC infotech"
    def showlanguage(self):
        print(f"the name of the employee is {f.name} and is good with  {self.language}")
        
a=employee()
b=programmer()

print(a.company,b.company)
    
    