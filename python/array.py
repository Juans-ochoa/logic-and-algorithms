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
