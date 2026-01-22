'''Write a program to check if a given word is a palindrome'''
a=str(input("Enter a word: "))
if a==a[::-1]:
    print("the given word is a palindrome")
else:
    print("the given word is not a palindrome")