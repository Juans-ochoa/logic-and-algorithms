def ternarySearch(arr: list, low: int, hight: int, k: int) -> int:
    if hight >= low:
        mid1 = low + (hight - low) // 3
        mid2 = hight - (hight - low) // 3

        if arr[mid1] == k:
            return mid1

        if arr[mid2] == k:
            return mid2

        if k < arr[mid1]:
            return ternarySearch(arr, low, mid1 - 1, k)
        elif k > arr[mid2]:
            return ternarySearch(arr, mid2 + 1, hight, k)
        else:
            return ternarySearch(arr, mid1+1, mid2-1, k)

    return -1


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(ternarySearch(arr, 0, len(arr) - 1, 5))

# Time Complexity: O(2 * log3n)
# Auxiliary Space: O(log3n)


def ternarySearchWhile(arr, low, hight, k):
    while hight >= low:
        mid1 = low + (hight - low) // 3
        mid2 = hight - (hight - low) // 3

        if k == arr[mid1]:
            return mid1
        if k == arr[mid2]:
            return mid2

        if k < arr[mid1]:
            hight = mid1 - 1
        elif k > arr[mid2]:
            low = mid2 + 1
        else:
            low = mid1 + 1
            hight = mid2 - 1

    return -1


print(ternarySearchWhile(arr, 0, len(arr)-1, 5))
# Time Complexity: O(2 * log3n), where n is the size of the array.
# Auxiliary Space: O(1)
