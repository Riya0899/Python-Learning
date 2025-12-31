 
class Employee:
    language="python"  # this is class artribute
    salary=120000
   
    def __init__(self,name,salary,language):  # dunder method which is automatically called
         self.name=name
         self.language=language            # giving paramenters will set the instance attributes
         self.salary=salary
         print("i am creating an object")
        
        
    def getinfo(self):   
       
        
        print(f"language is {self.language} and salary is {self.salary}")
    
    # if we dont want to pass  object in function
    @staticmethod
    def greet():
        print("good morning")

obj=Employee("harry",13000,"java")   # giving parameters in init means you need to add arguments in the objects whenver u call

print(obj.name,obj.salary)



