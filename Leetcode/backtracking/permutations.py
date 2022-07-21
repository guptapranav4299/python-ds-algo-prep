"""
46. Permutations
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:

Input: nums = [1]
Output: [[1]]



Constraints:

    1 <= nums.length <= 6
    -10 <= nums[i] <= 10
    All the integers of nums are unique.

"""



from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        if len(nums) == 1:
             result.append(nums[:])

        for i in range(len(nums)):
            temp = nums.pop(0)
            permutations = self.permute(nums)

            for permutation in permutations:
                permutation.append(temp)
            result.extend(permutations)
            nums.append(temp)

        return result


if __name__ == "__main__":
    obj = Solution()
    arr = [1, 2, 3]
    print(obj.permute(arr))