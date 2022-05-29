'''def attendance(n):
    x=[23,45,67,33,57,90,2]
    if n in x:
        print("Present")
    else:
        print("Absent")

n=int(input("Enter roll number"))
attendance(n)'''

'''def county(val):
    vov=0
    con=0
    for i in range(len(val)):
        if val[i] in ['a','e','i','o','u']:
            vov=vov+1
        else:
            con=con+1
    print("Vowels",vov)
    print("Consonants",con)
x=input("Enter")
county(x)'''

'''def factorial(num):
    fact=1
    while(num!=0):
        fact*=num
        num=num-1
    print("Factorial is",fact)
num=int(input("Enter a number"))
factorial(num)'''

'''def response(text):
    z=text.upper()
    print(z)
text=input("Enter string:")
response(text)'''

from time import *
sleep(10)
print('Hello')
sleep(3)
print("Hello")
