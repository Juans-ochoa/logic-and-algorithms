# Count subarrays with all elements greater than K
# Given an array of n integers and an integer k, the task is to find the number of subarrays such that all elements in each subarray are greater than k.
def countSubArrays(arr: list, k: int) -> int:
    count = left = right = 0
    lenArr = len(arr) - 1

    while left <= lenArr and right <= lenArr:
        if arr[left] > k and arr[right] > k:
            right += 1
            count += 1
        else:
            left += 1
            right = left

    return count + 1


def otherCountSubArrays(arr: list, k: int) -> int:
    count, start = 0
    n = len(arr)

    for end in range(n):
        if arr[end] <= k:
            start = end + 1
            continue

        count += end - start + 1


countSubArrays([3, 4, 5, 6, 7, 2, 10, 11], 5)
