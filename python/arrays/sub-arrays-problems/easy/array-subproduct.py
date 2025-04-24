# Check if subarray with given product exists in an array

# Given an array of both positive and negative integers and a number K., The task is to check if any subarray with product K is present in the array or not.

def hasSubArrayWithProduct(arr, k) -> str:
    length = len(arr)

    for i in range(length):
        prod = 1

        for j in range(i, length):
            prod *= arr[j]

            if prod == k:
                return 'YES'
    return 'No'


print(hasSubArrayWithProduct([1, 2, -5, -4], -10))
