# Write a Python program to implement the Selection Sort algorithm.
def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr
arr = list(map(int, input("Enter numbers separated by space: ").split()))
sorted_arr = selection_sort(arr)
print("Sorted array:", sorted_arr)