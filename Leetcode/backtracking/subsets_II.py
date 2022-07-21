"""
90. Subsets 2
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:

Input: nums = [0]
Output: [[],[0]]


Constraints:

    1 <= nums.length <= 10
    -10 <= nums[i] <= 10
"""

from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        def backtrack(idx, subset):
            if idx == len(nums):
                result.append(subset[::])
                return

            #             number included
            subset.append(nums[idx])
            backtrack(idx + 1, subset)
            subset.pop()

            #             number not included
            while idx + 1 < len(nums) and nums[idx] == nums[idx + 1]:
                idx += 1
            backtrack(idx + 1, subset)

        backtrack(0, [])
        return result


if __name__ == "__main__":
    obj = Solution()
    arr = [1, 2, 2]
    print(obj.subsetsWithDup(arr))
