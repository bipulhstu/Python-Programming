def main():
    func(1)
    func(3)
    func(5)
def func(a):
    for i in range(a, 10):
        print(i, end=" ")
    print()
if __name__=="__main__":
    main()