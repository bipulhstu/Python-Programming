#Declaring a variable and initialize it
number = 10
print(number)

#re-declaring the variable works
number = "Bipul Islam"
print(number)

#concatenate variables
a = "Bipul"
b = 145
print(a+str(b))

#Local Variable vs Global Variable
#declare a variable and initialize it
f = 101 #Global variable
print (f)
#declare a function
def someFunction():
    f = "I am learning python" #local variable
    print(f)
someFunction() #prints local variable
print(f)       #prints global variable
