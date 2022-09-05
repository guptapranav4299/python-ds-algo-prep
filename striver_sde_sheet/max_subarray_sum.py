"""
53. Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:

Input: nums = [1]
Output: 1

Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23

Constraints:

    1 <= nums.length <= 105
    -104 <= nums[i] <= 104

Follow up: If you have figured out the O(n) solution, try coding another solution using
the divide and conquer approach, which is more subtle.

"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]  # Keep track of max sub-array sum
        curSum = 0  # Keep track of current sub-array sum

        for num in nums:
            if curSum + num < num:
                curSum = num  # Start a new sub-array
            else:
                curSum = curSum + num  # Extend from our previous sub-array
            maxSum = max(maxSum, curSum)
        return maxSum