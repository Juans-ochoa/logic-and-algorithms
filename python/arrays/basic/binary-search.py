def binarySearch(arr: list, x) -> int:
    low = 0
    hight = len(arr) - 1

    while low <= hight:
        mid = low + (hight - low) // 2

        if arr[mid] == x:
            return mid

        elif arr[mid] < x:
            low = mid + 1
        else:
            hight = mid - 1

    return -1


arr = [2, 3, 4, 10, 40]
x = 10

print(binarySearch(arr, x))


def binarySearchRecursive(arr, low, hight, x) -> int:
    if hight >= low:
        mid = low + (hight - low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearchRecursive(arr, low, mid - 1, x)
        else:
            return binarySearchRecursive(arr, mid+1, hight, x)
    else:
        return -1


res = binarySearchRecursive(arr, 0, len(arr)-1, x)
print(res)
