# Alternate elements of an array
# Given an array arr[], the task is to print every alternate element of the array starting from the first element.

# Input: arr[] = [10, 20, 30, 40, 50]
# Output: 10 30 50

def getAlternates(arr: list) -> list:
    res = []

    for i in range(0, len(arr), 2):
        res.append(arr[i])

    return res

# Time Complexity: O(n), where n is the number of elements in arr[].
# Auxiliary Space: O(1)


arr = [10, 20, 30, 40, 50]

print(getAlternates(arr))

# Recursive Approach


def getAlternatesRecursive(arr: list, index=0, resp=[]) -> list:
    if index < len(arr):
        resp.append(arr[index])
        getAlternatesRecursive(arr, index+2, resp)

    return resp


# Time Complexity: O(n), where n is the number of elements in arr[].
# Auxiliary Space: O(n), for recursive call stack.
print(getAlternatesRecursive(arr))
