# wap to identify whether a file isw identical and matched another file's content or not

with open("file1.txt") as f:
    content1=f.read()
    
with open("file2.txt") as f:
    content2=f.read()
    
if(content1==content2):
    print("files are identical")
else:
    print("files are not identical")