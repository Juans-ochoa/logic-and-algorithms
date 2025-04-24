def sortedArray(arr):
    left = 0
    right = len(arr) - 1
    count = 0

    while count <= len(arr) and left <= right:
        if arr[left] < arr[left+1]:
            left += 1

        if arr[right] > arr[right - 1]:
            right -= 1

        count += 1

    while left < right:
        if arr[left] > arr[right]:
            arr[left], arr[right] = arr[right], arr[left]

        left += 1
        right -= 1

    print(arr)


sortedArray([1, 7, 6,  5, 4, 8])
sortedArray([1, 7, 6, 5, 4, 3, 2, 8])
