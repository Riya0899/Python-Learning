# wap function to remove a given word from the list and strip it at the same time
def rem(l):
    for item in l:
        l.remove(word)
        return l
        
l=["harry","riya","shubh","an"]

word=input("enter teh word you want to remove")
print(rem(l))