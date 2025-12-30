s11={1,2,3,4,5,5,5,5,"riya"}
s11.add("shubham")
print(s11) 

# operations
print(s11.__len__()) # return length

s11.remove(2) # remobe item
print(s11)

print(s11.pop())
print(s11.clear())

# UNION AND INTERSECTION

s1={1,23,12,65,76,35}
s2={1,23,10,61,74,75}

print(s1.union(s2)) # all values without repetetion
print(s1.intersection(s2)) # common values