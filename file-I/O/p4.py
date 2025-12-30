word="donkey"

with open("text.txt",'r') as f:
    content=f.read()
    
contentNew=content.replace("donkey","####")

with open("text.txt",'w') as f:
    f.write(contentNew)