# Split an array into two equal Sum subarrays

# Given an array of integers greater than zero, find if it is possible to split it in two subarrays (without reordering the elements), such that the sum of the two subarrays is the same. Print the two subarrays.

def findSplitPoint(arr):
    leftSum = 0
    lengthArr = len(arr)
    indexArr = -1

    for i in range(0, lengthArr):
        leftSum += arr[i]

        rightSum = 0
        for j in range(i+1, lengthArr):
            rightSum += arr[j]

        if leftSum == rightSum:
            indexArr = i+1
            break

    if indexArr == -1 or indexArr == lengthArr:
        print('Is not posible split in two sub arrays')
    else:
        print(arr[:indexArr])
        print(arr[indexArr:])


findSplitPoint([1, 2, 3, 4, 6, 5])
