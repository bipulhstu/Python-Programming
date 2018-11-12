def myfunc(x):
    print("inside myfunc ",x)
    x = 10  #local variable
    print("inside myfunc ",x)
def main():
    x =20 #global variable
    myfunc(x)
    print(x)
if __name__=="__main__": main()