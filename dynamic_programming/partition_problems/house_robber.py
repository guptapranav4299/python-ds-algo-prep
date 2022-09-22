"""
198. House Robber

You are a professional robber planning to rob houses along a street. Each
house has a certain amount of money stashed, the only constraint stopping you from robbing
each of them is that adjacent houses have security systems connected and it will automatically
contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the
maximum amount of money you can rob tonight without alerting the police.



Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.



Constraints:

    1 <= nums.length <= 100
    0 <= nums[i] <= 400


"""


class Solution:
    # time - 0(n ^ 2) space - 0(n)
    def recursive(self, nums, i):
        if i >= len(nums):
            return 0
        ans = 0
        ans = max(self.recursive(nums, i + 1), (self.recursive(nums, i + 2) + nums[i]))
        return ans

    # time - 0(n) space - 0(n)
    def memoize(self, nums, i, memo):
        if i >= len(nums):
            return 0
        if memo[i] != -1:
            return memo[i]
        memo[i] = max(self.memoize(nums, i + 1, memo), (self.memoize(nums, i + 2, memo) + nums[i]))
        return memo[i]

    # time - 0(n) space - 0(n)
    def tabular(self, nums):
        n = len(nums)
        if n <= 2:
            return max(nums)

        dp = [0 for i in range(n)]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[n - 1]


if __name__ == "__main__":
    obj = Solution()
    nums =[1, 2, 3, 1]
    print(obj.recursive(nums, 0))
    dp = [ -1 for i in range(len(nums) + 1)]
    print(obj.memoize(nums, 0, dp))
    print(obj.tabular(nums))