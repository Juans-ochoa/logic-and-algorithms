def binarySearch(arr: list, low: int, hight: int, k: int):
    if low <= hight:
        mid = low + (hight - low) // 2
        if arr[mid] == k:
            return mid

        if arr[mid] > k:
            return binarySearch(arr, low, mid-1, k)
        else:
            return binarySearch(arr, mid+1, hight, k)

    return -1


def exponentialSearch(arr: list, k: int):
    if arr[0] == k:
        return 0

    n = len(arr) - 1
    i = 1

    while i <= n and arr[i] <= k:
        i = i * 2

    return binarySearch(arr, i // 2, min(i, n), k)


arr = [2, 3, 4, 10, 40]
x = 10
result = exponentialSearch(arr, x)
if result == -1:
    print("Element not found in the array")
else:
    print("Element is present at index %d" % (result))
