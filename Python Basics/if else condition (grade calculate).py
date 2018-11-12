marks = input("Enter your marks: ")
marks = int(marks)

if marks>=80:
    print("You got A+");
elif marks >=70:
    print("You got A grade");
elif marks >=60:
    print("You got B grade");
elif marks>=50:
    print("You got C grade");
elif marks>=40:
    print("You got D grade");
else:
    print("You failed!!!");
