"""
131. Palindrome Partitioning

Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.
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
        table = [[] for _ in s]
        table[0].append([s[0]])
        for i, ch in enumerate(s[1:]):
            for item in table[i]:
                # Single character
                table[i+1].append(item + [ch])
                # palindrome of 2 chars
                if len(item) >= 1 and len(item[-1]) == 1 and item[-1] == ch:
                    temp = item[-1] + ch
                    table[i+1].append(item[:-1] + [temp])
                # Palindrome of >2 chars
                if len(item) >= 2 and len(item[-2]) == 1 and item[-2] == ch:
                    temp = item[-2] + item[-1] + ch
                    table[i+1].append(item[:-2] + [temp])
        return table[-1]