def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
arr=[89,45,68,90,29,34,17]
bubblesort(arr)
print("Sorted array: ",arr)