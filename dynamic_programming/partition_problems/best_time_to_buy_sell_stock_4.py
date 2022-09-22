from typing import List


class Solution:
    # time - 0(2 ^ n) space - 0(n)
    def maxProfit(self, k: int, prices: List[int]) -> int:
        def recur(i, buy, k , prices):
            if i == len(prices):
                return 0
            ans = recur(i+1, buy, k, prices)
            if k == 0:
                return 0
            if buy:
                ans = max(ans, recur(i + 1, False, k, prices) - prices[i] )
            else:
                ans = max(ans, recur(i + 1, True, k - 1, prices) + prices[i])
            return ans
        return recur(0,True, k, prices)

    # time - o(n) space - 0(2 * n * k) + 0(n) [call stack]
    def maxProfit_2(self, k: int, prices: List[int]) -> int:
        def memoize(i, buy, k , prices, memo):
            if i == len(prices):
                return 0
            if memo[i][buy][k] != -1:
                return memo[i][buy][k]
            ans = memoize(i+1, buy, k, prices, memo)
            if k == 0:
                return 0
            if buy:
                ans = max(ans, memoize(i + 1, False, k, prices, memo) - prices[i] )
            else:
                ans = max(ans, memoize(i + 1, True, k - 1, prices, memo) + prices[i])
            memo[i][buy][k] = ans
            return ans
        n = len(prices)
        memo = [[[-1 for i in range(k + 1)]for i in range(2)] for i in range(n + 1)]
        return memoize(0,True, k, prices, memo)

    # time - 0(n * k) space - 0(n * k)
    def tabulation_approach(self, prices, k):
        n, ans = len(prices), 0
        dp = [[[0, -99999] for i in range(k + 1)] for i in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, k + 1):
                dp[i][j][0] = max(max(dp[i - 1][j][0], dp[i - 1][j - 1][0]), prices[i - 1] + dp[i - 1][j][1])
                if j <= i:
                    dp[i][j][1] = max(dp[i - 1][j][1], -prices[i - 1] + dp[i - 1][j - 1][0])
                ans = max(ans, dp[i][j][0])
        return ans