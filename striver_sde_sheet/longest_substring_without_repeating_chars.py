"""
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.



Constraints:

    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.

"""


class Solution:
    """
    Approach - 2
    Using sliding window technique, shrink the
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        longest = 0
        s_set = set()
        l = 0
        for i in range(n):
            while s[i] in s_set:
                s_set.remove(s[l])
                l += 1
            s_set.add(s[i])
            longest = max(longest, i - l + 1)

        return longest