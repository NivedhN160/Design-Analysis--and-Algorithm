'''Write a python program to find the largest of 3 numbers'''
a=int(input("Enter a number a: "))
b=int(input("Enter a number b: "))
c=int(input("Enter a number c: "))
if a>b and a>c:
    print("A is greater")
elif b>a and b>c:
    print("B is greater")
else:
    print("C is greater")