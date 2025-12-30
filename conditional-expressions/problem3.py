sub1=int(input("enter your marks in subject1 "))
sub2=int(input("enter your marks in subject2 "))
sub3=int(input("enter your marks in subject3 "))

percnt=((sub1+sub2+sub3)/300)*100

if(percnt>=40 and sub1>33 and sub2>33 and sub3>33):
    print("you are pass")

else:
    print("you are fail")