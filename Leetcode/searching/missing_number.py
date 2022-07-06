"""
Q.268
Given an array nums containing n distinct numbers in the range[0, n], return the only number in the range that is missing from the array.

Example1:

Input: nums = [3, 0, 1]
Output: 2

Example 2:

Input: nums = [0, 1]
Output: 2

Example 3:

Input: nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
Output: 8

Constraints:
n == nums.length
1 <= n <= 104
0 <= nums[i] <= n
All the numbers of nums are unique.
"""
from typing import List


class Solution:


    def missingNumber2(self,nums):
        try:
            nums.sort()
            for i in range(0,len(nums)):
                if nums[i] != i:
                    return i
                else:
                    pass
            return len(nums)
        except Exception as e:
            raise Exception("Error in missing number2---->",str(e))
    # o(1)
    def missingNumber(self, nums: List[int]) -> int:
        try:
            n = len(nums)
            return (n*(n+1)//2) - sum(nums)
        except Exception as e:
            raise Exception("Error in missing number 1-------->",str(e))


if __name__ == "__main__":
    obj = Solution()
    arr = [0,1]
    print(obj.missingNumber(arr))
    print(obj.missingNumber2(arr))
