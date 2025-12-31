# wap to rename a file 

with open("file1.txt") as f:
    content=f.read()
    
with open("file2.txt",'w') as f:
    f.write(content)