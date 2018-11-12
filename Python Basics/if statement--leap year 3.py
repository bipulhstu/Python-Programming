year= input("Please, Enter a year to check it is leap year or not: ")
year = int(year)

if  year %100 !=0 and year%4 == 0:
    print("Yes")
elif year % 100 == 0 and year %400 ==0:
    print("Yes")
else:
    print("No")
    

print("Program terminated")
