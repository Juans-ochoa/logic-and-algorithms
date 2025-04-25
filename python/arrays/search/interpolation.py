def interpolationSearch(arr: list, lo: int, hi: int, x):
    if (lo <= hi) and (x >= arr[lo]) and (x <= arr[hi]):
        pos = lo + (((x - arr[lo])*(hi - lo))//(arr[hi] - arr[lo]))

        if arr[pos] == x:
            return pos

        if arr[pos] < x:
            return interpolationSearch(arr, pos + 1, hi, x)

        if arr[pos] > x:
            return interpolationSearch(arr, lo, pos - 1, x)

    return -1


arr = [10, 12, 13, 16, 18, 19, 20,
       21, 22, 23, 24, 33, 35, 42, 47]
n = len(arr) - 1

# Element to be searched
x = 18
index = interpolationSearch(arr, 0, n, x)

if index != -1:
    print("Element found at index", index)
else:
    print("Element not found")

# Time Complexity: O(log2(log2 n)) for the average case, and O(n) for the worst case
# Auxiliary Space Complexity: O(1)


def interpolationSearchWhile(arr: list, x: int):
    hi = len(arr) - 1
    lo = 0

    while lo <= hi and x >= arr[lo] and x <= arr[hi]:
        if lo == hi:
            if arr[lo] == x:
                return lo
            return -1
        pos = lo + (((x - arr[lo])*(hi - lo))//(arr[hi] - arr[lo]))

        if arr[pos] == x:
            return pos

        if arr[pos] < x:
            lo = pos + 1
        else:
            hi = pos - 1

    return -1

# Time Complexity: O(log2(log2 n)) for the average case, and O(n) for the worst case
# Auxiliary Space Complexity: O(1)
