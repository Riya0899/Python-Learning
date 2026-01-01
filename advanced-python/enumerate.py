l= [11,222,123,134,454]

# index=0
# for item in l:
#     print(f"the item at index {index} is {item}")
#     index+=1
    
# this can be simplified using enumerate function

for index,item in enumerate(l):
    print(f"the item at index {index} is {item}")