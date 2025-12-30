marks={
    "riya":10,
    "shubham":23
}
print(marks.items()) # display all items
print(marks.keys()) # display all keys
print(marks.values()) # display all values
marks.update({"riya":20 , "renuka":20}) #update dictionary
print(marks)
print(marks.get("shubham")) # get value

print(marks.get("shubh2")) # prints none
print(marks["shubh2"]) # returns an error