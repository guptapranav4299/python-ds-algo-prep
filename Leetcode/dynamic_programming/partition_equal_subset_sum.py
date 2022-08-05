"""
416. Partition Equal Subset Sum

Given a non-empty array nums containing only positive integers,
find if the array can be partitioned into two subsets such that the sum of elements in both subsets
is equal.


Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.



Constraints:

    1 <= nums.length <= 200
    1 <= nums[i] <= 100

"""

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum=sum(nums)
        if total_sum%2!=0:
            return False
        tgt_sum=total_sum//2
        dp=[False for i in range(tgt_sum+1)]
        dp[0]=True
        for i in nums:
            for j in range(len(dp)-1,i-1,-1):
                if dp[j-i]:
                    dp[j]=True
        return dp[-1]


if __name__ == "__main__":
    obj = Solution()
    nums = [1,5,11,5]
    print(obj.canPartition(nums))