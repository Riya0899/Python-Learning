
class Employee:
    language="python"  # this is class artribute
    salary=120000
    

obj=Employee()
obj.language="javascript"  # this is instance attribute
print(obj.language,obj.salary)

# instance attributes takes more preference than class attributes dueing assignment or retreival