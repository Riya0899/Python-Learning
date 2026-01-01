class employee:
    a=1
    
    @classmethod   # this will show class attribute in output 
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

e=employee()
e.a=19 

e.show()      