"""
131. Palindrome Partitioning

Given a string s, partition s such that every substring of the partition is a palindrome.
Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:

Input: s = "a"
Output: [["a"]]



Constraints:

    1 <= s.length <= 16
    s contains only lowercase English letters.

"""
from typing import List


class Solution:

    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(s):
            return s == s[::-1]

        def recur(idx, res=[], ans=[]):
            if idx >= len(s):
                ans.append(res[:])
                return
            for j in range(idx, len(s)):
                if is_palindrome(s[idx:j + 1]):
                    res.append(s[idx:j + 1])
                    recur(j + 1)
                    res.pop()
            return ans
        return recur(0)

    # bottom up
    def partition_2(self, s: str) -> List[List[str]]:
        dp = []
        n = len(s)

        for i in range(n + 1):
            dp.append([])  # create dp of size n+1

        dp[-1].append([])  # because for s[n:] i.e. empty string ,  answer = [[]]

        # dp[i] store all possible palindrome partitions of string s[i:]

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n + 1):
                curr = s[i:j]  # cosider each substring of s start from i-th character

                if curr == curr[::-1]:  # if substring is palindrome

                    # Consider first element of each partition is curr then add curr in the front of all partitions of string s[j:]  , which are already stored in dp[j]
                    for e in dp[j]:
                        dp[i].append([curr] + e)

        return dp[0]  # All palindrome partitions of s[0:] = s


if __name__ == "__main__":
    obj = Solution()
    s = "aab"
    print(obj.partition(s))
    print(obj.partition_2(s))