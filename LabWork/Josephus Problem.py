# Write a Python program to simulate the Josephus Problem.
def josephus(n, k):
    people = list(range(1, n + 1))
    index = 0
    while len(people) > 1:
        index = (index + k - 1) % len(people)
        people.pop(index)
    return people[0]
n = int(input("Enter number of people: "))
k = int(input("Enter step count: "))
survivor = josephus(n, k)
print("The safe position is:", survivor)