name="riya" # this is a string

# to slice a string

s1=name[1:3] #[starting index : ending index]
# start from the index 1 all the way till 3 excluding 3
print(s1)

s2=name[-4:-1] 
s2=name[0:3] 

# these two re same just start counting from rhs in case of negative starting from -1
name[:4] # same as 0:4
name[1:] # same as 1:length

# slicing with skip values 

word="abcdefghijklmnop"
sliced=word[2:8:3]
# start from index 2 all the way till 4 skipping 3 values in between
print(sliced) 