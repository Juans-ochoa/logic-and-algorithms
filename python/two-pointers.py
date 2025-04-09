# def isPalindrome(s:str)->bool:
#     left = 0
#     right = len(s) -1

#     while left < right:
#         if s[left] != s[right]: return False
#         left += 1
#         right -= 1

#     return True

# print(isPalindrome("abba"))

# def checkForTarget(arr:list, target:int)->bool:
#     left = 0
#     right = len(arr) -1

#     while left< right:
#         current = arr[left] + arr[right]
#         if current == target: return True
#         if current > target: right -= 1
#         else: left += 1
#     return False

# print(checkForTarget([1,2,4,5], 6))

def combine(arr1:list, arr2:list)->list:
    result = []
    i = j = 0

    while i<len(arr1) and j<len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i+=1
        else:
            result.append(arr2[j])
            j+=1
    

    while i < len(arr1):
        result.append(arr1[i])
        i+=1
    
    while j< len(arr2):
        result.append(arr2[j])
        j+=1

    return result

print(combine([1,3,4], [2,4,6,9]))