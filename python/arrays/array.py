# Techniques
# Sliding window
"""
Problem: Given an array of integers, find the maximum sum of a subarray with a fixed window size.
"""
# def maxSubArraySum(nums: list, k: int) -> int:
#     maxValue = float('-inf')
#     windowLength = k - 1
#     currentRunningSum = 0
#     print('Window length: ', windowLength)

#     for i in range(len(nums)):
#         currentRunningSum += nums[i]

#         if i >= k - 1:
#             maxValue = max(maxValue, currentRunningSum)
#             currentRunningSum -= nums[i - windowLength]

#     return maxValue


# maxSubArraySum([2, 1, 5, 1, 3, 2], 3)

"""
Maximum Sum Subarray of Size K
Given an array of positive integers and a positive number k, find the maximum sum of any contiguous subarray of size k.
"""
# def getMaxSum(nums: list, k: int):
#     maxSumValue = float('-inf')
#     sumRunning = 0
#     windowLength = k - 1

#     for i in range(len(nums)):
#         sumRunning += nums[i]

#         if i >= windowLength:
#             maxSumValue = max(maxSumValue, sumRunning)
#             sumRunning -= nums[i - windowLength]
#     return maxSumValue

# print(getMaxSum([3, 5, 2, 1, 7, 2], 2))
