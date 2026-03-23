# Write a Python program to solve the Fake Coin Problem using a divide-and-conquer approach.

def find_fake_coin(coins, left, right):
    if left == right:
        return left
    mid = (left + right) // 2
    left_half = coins[left:mid+1]
    right_half = coins[mid+1:right+1]
    if sum(left_half) < sum(right_half):
        return find_fake_coin(coins, left, mid)
    elif sum(left_half) > sum(right_half):
        return find_fake_coin(coins, mid+1, right)
    else:
        return -1
coins = list(map(int, input("Enter coin weights separated by space: ").split()))

index = find_fake_coin(coins, 0, len(coins) - 1)

if index != -1:
    print("Fake coin found at position:", index)
else:
    print("No fake coin detected")