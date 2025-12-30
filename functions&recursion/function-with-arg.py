# functions with argument

def greet(name,ending): 

    print("good morning "+ name)
    print(ending)
    
greet("harry","thankyou")

## functions with default parameters

def greet(name,ending="thankyou"): 
    print("good morning "+ name)
    print(ending)
    
greet("harry")