class employee:
    company="ITC"
    salary=12000
    def show(self):
        print(f"the name of the employee is {self.company} and salary is {self.salary}")
        
class coder:
    language="python"
    
    def printlanguage(self):
        print(f"here is your language {self.language}")
        
        
class programmer(employee,coder):
    company="ITC infotech"
    def showlanguage(self):
        print(f"the name of the employee is {self.company} and is good with  {self.language}")
        
a=employee()
b=programmer()

b.show()
b.showlanguage()
b.printlanguage()    
    