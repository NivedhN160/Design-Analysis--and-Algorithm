'''Write a program for sequential search'''
a=[1,2,3,4,5,6,7,8,9]
b=int(input("Enter the number to be searched:"))
for i in range(0,len(a)):
    if b==a[i]:
        print("The number was found")
        break
else:
    print("The number was not found")