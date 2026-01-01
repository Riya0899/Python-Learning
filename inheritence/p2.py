class animals:
    def __init__(self,name):
        self.name=name
    def show(self,name):
        print(f"the animal is {self.name}")
        
class pets(animals):
    def pet(self):
        print("there are many animals for the option to pet")
        
class dog(pets):
    def bark(self):
        print(f"{self.name} barks")
        
a=animals("gabbu")
b=pets("gabbu")
c=dog("gabbu")
c.bark()

        
