"""
188. Best Time to Buy and Sell Stock IV

You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.

Find the maximum profit you can achieve. You may complete at most k transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).



Example 1:

Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.

Example 2:

Input: k = 2, prices = [3,2,6,5,0,3]
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.



Constraints:

    0 <= k <= 100
    0 <= prices.length <= 1000
    0 <= prices[i] <= 1000


"""


from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:

        def dp(idx, buy, k, prices):
            if idx == len(prices):
                return 0
            if memo[idx][buy][k] != -1:
                return memo[idx][buy][k]
            # neither buy nor sell
            ans = dp(idx + 1, buy, k , prices)
            if k == 0:
                return 0
            if buy:
                ans = max(ans, dp(idx+1, False, k, prices) - prices[idx])
            else:
                ans = max(ans, dp(idx+1, True, k - 1, prices) + prices[idx])

            memo[idx][buy][k] = ans
            return ans
        n = len(prices)
        memo = [[[-1 for i in range(k+1)] for i in range(2)] for i in range(n)]
        return dp(0, True, k, prices)


if __name__ == "__main__":
    obj = Solution()
    prices = [3,2,6,5,0,3]
    k = 2
    print(obj.maxProfit(k , prices))