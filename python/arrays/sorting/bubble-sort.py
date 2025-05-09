def bubbleSort(arr: list) -> list:
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        if not swapped:
            break


arr = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(arr)

print("Sorted array:")
for i in range(len(arr)):
    print("%d" % arr[i], end=" ")

# Time Complexity: O(n2)
# Auxiliary Space: O(1)
