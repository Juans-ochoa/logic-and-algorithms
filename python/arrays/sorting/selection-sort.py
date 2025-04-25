def selectionSort(arr: list):
    l = len(arr)

    for i in range(l - 1):
        min_idx = i

        for j in range(i+1, l):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]


def print_array(arr):
    for val in arr:
        print(val, end=" ")
    print()


arr = [64, 25, 12, 22, 11]

print("Original array: ", end="")
print_array(arr)

selectionSort(arr)

print("Sorted array: ", end="")
print_array(arr)
# Time Complexity: O(n2)
# Auxiliary Space: O(1)


def minIndex(arr: list, i: int, j: int) -> int:
    if i == j:
        return i

    k = minIndex(arr, i + 1, j)

    return (i if arr[i] < arr[k] else k)


def recursiveSelectionSort(arr: list, n: int, index: int = 0):
    if index == n:
        return -1

    k = minIndex(arr, index, n - 1)

    if k != index:
        arr[k], arr[index] = arr[index], arr[k]

    recursiveSelectionSort(arr, n, index+1)


# Driver code
arr2 = [3, 1, 5, 2, 7, 0]
n = len(arr)

print('Unsorted Array')
print_array(arr2)
# Calling function
recursiveSelectionSort(arr2, n)

print('Sorted Array')
print_array(arr2)
