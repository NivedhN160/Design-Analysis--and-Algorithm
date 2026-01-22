'''Write a program to check if the given number is a prime number'''
n = int(input("Enter a number: "))
if n<1:
    print("the given number is not a prime number")
else:
    for i in range(2,n):
        if n%i==0:
            print("the given number is not a prime number")
            break
        else:
            print("the given number is a prime number")
            break