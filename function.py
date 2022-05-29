import time
while(1):   
    def add(n,m):
        print(n+m)
    def sub(n,m):
        if n>m:
            return(n-m)
        else:
            return(m-n)
    def prod(n,m):
        print(m*n)
    def division(n,m):
        print(n/m)

    print("1...Addition")
    print("2...Substraction")
    print("3...Multiplication")
    print("4...Divide")
    print("5...Exit")
    x=int(input("Enter your choice"))
    if x==1:
        a=int(input("Enter 1st number"))
        b=int(input("Enter 2nd number"))
        add(a,b)
    elif x==2:
        a=int(input("Enter 1st number"))
        b=int(input("Enter 2nd number"))
        print("Subtraction=",sub(a,b))
    elif x==3:
        a=int(input("Enter 1st number"))
        b=int(input("Enter 2nd number"))
        prod(a,b)
    elif x==4:
        division(10,20)
    elif x==5:
        print("Exiting")
        time.sleep(10)
        break