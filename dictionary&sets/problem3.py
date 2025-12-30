# CREATE AN EMPTY DICTIONARY.ALLOW 4 FRIENDS TO ENTER THEIR FAVOURITE LANGUAGE AS VALUE AND USE KEY AS THEIR NAMES.ASSSUME THAT THE NAMES ARE UNIQUE

dict={}

name1=input("enter language name")
lang1=input("enter language")
dict.update({name1:lang1})
name2=input("enter language name")
lang2=input("enter language")
dict.update({name2:lang2})
name3=input("enter language name")
lang3=input("enter language")
dict.update({name3:lang3})
name4=input("enter language name")
lang4=input("enter language")
dict.update({name4:lang4})

print(dict)