# convert celcious into ferhnhite
# c=5*(f-32)9

def ftoc(f):
    c=5*(f-32)/9
    print(f"temp in celcious is {c}")

f=int(input("enter temp in fernhite"))
ftoc(f)
      