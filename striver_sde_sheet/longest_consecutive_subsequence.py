"""
128. Longest Consecutive Sequence

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.



Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9



Constraints:

    0 <= nums.length <= 105
    -109 <= nums[i] <= 109


"""


from typing import List


class Solution:
    """
    Naive Approach -
    Sort the array and then search for the longest sequence.
    """
    def naive_approach(self, nums):
        nums.sort()
        longest = 0
        for n in nums:
            if n - 1 not in nums:
                length = 0
                while(n + length) in nums:
                    length += 1
                longest = max(longest, length)
        return longest


    """
    Aprroach - 2
    Store elements in hashset and then iterate over the elements in the array. Check if n -1 doesnt
    exists in the hashset. Then we check n + 1 element in the hashset if exists then again incease the
    counter. Store the max of the longest sequence and return the answer.

    Time - 0(N)
    Space - 0(N)
    """
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for n in nums:
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)

        return longest


if __name__ == "__main__":
    obj = Solution()
    # nums = [100,4,200,1,3,2]
    nums = [0,3,7,2,5,8,4,6,0,1]
    print(obj.naive_approach(nums))