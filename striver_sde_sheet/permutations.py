from typing import List


class Solution:
    """
    Approach - 1
    Pop the first element of the nums and then find permutations from the rest of the elements. Then append
    the popped element to the permutations list. Append the list in the result and then add the popped
    element back to the nums so that it can be used again for further permutations.
    If len(nums) == 1 which means there is single element then return that element.
    Time - 0(n^n!)
    Space - 0(n)
    """
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        if len(nums) == 1:
            res.append(nums[::])
        for i in range(len(nums)):
            temp = nums.pop(0)
            permutations = self.permute(nums)
            for permutation in permutations:
                permutation.append(temp)
            res.extend(permutations)
            nums.append(temp)
        return res
