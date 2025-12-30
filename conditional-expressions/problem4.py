# WAP TO FIND WHETHER A GIVEN USERNAME CONTAIN LESS THAN 10 CHARACTERS OR NOT

username=input("enter your username ")
characters=username.__len__()

if(characters<10):
    print("invalid username")
else:
    print("valid username")