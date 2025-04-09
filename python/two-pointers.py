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