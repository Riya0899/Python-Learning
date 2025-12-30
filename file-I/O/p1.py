with open("file.txt") as f:
    data=f.read()
    
if("twinkle" in data):
    print("the poem contains twinkle")
else:
    print("it doesnot contain twinkle")