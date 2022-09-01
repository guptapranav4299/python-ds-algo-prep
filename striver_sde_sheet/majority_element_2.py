"""

"""


class Solution:
    """
    Approach -  2
    Best approach
    WE will use moore's voting algo
    """
    def majorityElement(self, nums: List[int]) -> List[int]:
        res1, res2, count1, count2 = None, None, 0, 0

        for n in nums:
            if res1 == n:
                count1 += 1
            elif res2 == n:
                count2 += 1
            elif count1 == 0:
                res1 = n
                count1 += 1
            elif count2 == 0:
                res2 = n
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1

        return [c for c in [res1, res2] if nums.count(c) > (len(nums) // 3)]