year = input("Please, Enter a year to check it is leap year or not: ")
year = int(year)

if year % 4!=0:
    print("No")
else:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Yes")
        else:
            print("No")
    else:
        print("Yes")

print("Program terminated")
