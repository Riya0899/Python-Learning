class employee:
     salary=23234
     increment=20
     @property
     def salaryAfterIncrement(self):
         print(self.salary + self.salary * (self.increment/100))
     @salaryAfterIncrement.setter
     def salaryAfterIncrement(self,salary):
         self.increment=((salary/self.salary)-1)*100
         
e=employee()
# print(e.salaryAfterIncrement)
e.salaryAfterIncrement=2633330
print(e.increment)