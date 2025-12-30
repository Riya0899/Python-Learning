# A SPAM CONTENT IS DEFINED AS A TEXT CONATINING FOLLOWING KEYWORDS:
# "MAKE A LOT OF MONEY" "BUY NOW" "SUBSCRIBE THIS" "CLICK THIS"
# WAP  TO DETECT THESE ERRORS

a="MAKE A LOT OF MONEY"
b="BUY NOW"
c="SUBSCRIBE THIS"
d="CLICK THIS"

content=input("enter your content")
if((a in content) or (b in content) or (c in content) or (d in content)):
    print("it is a spam")
else:
    print("not a spam")
    