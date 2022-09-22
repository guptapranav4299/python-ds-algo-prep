from math import inf
from typing import List


class Solution:
    # tabulation
    def splitArray(self, nums: List[int], m: int) -> int:
        ps = []
        for v in nums:
            ps.append(v + (ps[-1] if len(ps) > 0 else 0))

        dp = [[0]*len(nums) for _ in range(m)]
        for i in range(m):
            for j in range(len(nums)):
                if i > 0:
                    min_val = inf
                    for k in range(j -1, i - 2, -1):
                        min_val = min(min_val, max(dp[i-1][k], ps[j] - ps[k]))
                        if ps[j] - ps[k] > dp[i-1][k]:
                            break
                    dp[i][j] = min_val
                else:
                    dp[i][j] = ps[j]
        return dp[i][j]

    # memoization
    def splitArray_2(self, nums: List[int], m: int) -> int:
        memo = [[-1 for i in range(m + 1)] for i in range(len(nums) + 1)]

        def dp(i, nums, m, memo):
            if i == len(nums):
                if m == 0:
                    return 0
                return 1000001
            if m <= 0:
                return 1000001
            if memo[i][m] != -1:
                return memo[i][m]
            ans = 1000001
            sum1 = 0
            for j in range(i, len(nums)):
                sum1 += nums[j]
                ans = min(ans, max(sum1, dp(j + 1, nums, m - 1, memo)))

            memo[i][m] = ans
            return ans

        return dp(0, nums, m, memo)

    # recursive (
    def splitArray_3(self, nums: List[int], m: int) -> int:
        def dp(i, nums, m):
            if i == len(nums):
                if m == 0:
                    return 0
                return 1000001
            if m <= 0:
                return 1000001
            ans = 1000001
            sum1 = 0
            for j in range(i, len(nums)):
                sum1 += nums[j]
                ans = min(ans, max(sum1, dp(j + 1, nums, m - 1)))

            return ans

        return dp(0, nums, m)