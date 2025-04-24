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
