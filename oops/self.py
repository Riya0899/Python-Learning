
class Employee:
    language="python"  # this is class artribute
    salary=120000
   
   # self is automatically passed with a function call from an object
    def getinfo(self):
        print(f"language is {self.language} and salary is {self.salary}")
    
    # if we dont want to pass  object in function
    @staticmethod
    def greet():
        print("good morning")

obj=Employee()
obj.getinfo( )
obj.greet()
# Employee.getinfo(obj)

