# wap which finds out whether a given name is present in a list or not

cars=["ford","toyota","hyundai","nano","maruti"]

car=input("enter the car you want to find")

if(car in cars):
    print("we have this car")
else:
    print("out of stock")