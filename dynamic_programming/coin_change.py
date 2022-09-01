"""
Given a value N and an integer vector COINS representing coins of different denominations.
Considering you have infinite supply of each coin, your task is to find total number of
combinations of these coins that make a sum of N. If that amount of money cannot be made up
by any combination of the coins, return 0.

"""


import math


class Solution:

    def bottom_up_approach(self, m, denoms):
        dp = [-1 for i in range(m + 1)]
        dp[0] = 0
        for i in range(1, m+1):
            dp[i] = 100000001
            for c in denoms:
                if i - c >=0 and dp[i - c] != 100000001:
                    dp[i] = min(dp[i], dp[i - c] + 1)

        if dp[m] == 100000001:
            return 0
        else:
            return dp[m]


if __name__ == "__main__":
    m = 8
    denom = [2, 5, 7, 10]
    obj = Solution()
    print(obj.bottom_up_approach(m,denom))