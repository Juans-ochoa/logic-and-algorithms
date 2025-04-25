def sentinelLinearSearch(arr: list, k: int) -> int:
    n = len(arr) - 1
    last = arr[n]
    arr[n] = k
    i = 0

    while arr[i] != k:
        i += 1

    arr[n] = last
    last = None

    if i < (n) or arr[n] == k:
        print(k, 'Is present at index: ', i)
        print(arr[i])
    else:
        print('The element is not present in the list!')


# Time Complexity: O(N)
# Auxiliary Space: O(1)
sentinelLinearSearch([10, 20, 180, 30, 60, 50, 110, 100, 70], 180)
