try:
    a=int(input("enter a number"))
    print(a)
except Exception as e:
    print(e)
    
# else:
#     print("you are inside else block")  # it will run when try is successful
    
finally:
    print("hey i am inside finally block")    # it will run for both ways