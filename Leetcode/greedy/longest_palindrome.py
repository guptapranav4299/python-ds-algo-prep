"""
409. Longest Palindrome

Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

Example 1:

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

Example 2:

Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.


Constraints:
    1 <= s.length <= 2000
    s consists of lowercase and/or uppercase English letters only.

"""
"""
Explanation:
let's say we have s = "abccccddd"
we will store the char and their frequency in a dictionary.
dict = {"a":1,"b":1,"c":4,"d":3}
to make a palindrome we will take max even occurences of every char. In our case 
longest palindrome ---> ccd.dcc
current dict =  {"a":1,"b":1,"c":0,"d":1}
To fill the . we can use anyone char that has frequency 1 or greater than 1 ie from (a,b,d). Lets say we add "a"
Longest Palindrome ----> "ccdadcc"
Hence its length will be 7

Algorithm:
1. Make a dictionary storing characters along with their frequency:
2. Check if length of dictionary is 1 then return the frequency of that character
3. Initialize 2 variables res and odd as 0. res will store the length of the longest palindrome and odd will store the no. of odd frequencies.
4. Iterate over the dictionary values:
    If frequency is greater than 1 then:
        Check if frequency modulo 2 is 0 if Yes:
            if Yes:
                Add the frequency to the res variable
            else:
                1. Add frequency - 1 to the res variable
                2. Add 1 to odd variable
        If No:
            Add frequency to the odd variable

5. Once loop ends If odd greater than 0  then add 1 to the res (for getting 1 odd frequency char)
6. Return the res variable
"""


class Solution:
    def longestPalindrome(self, s: str) -> int:
        letter_dict = {}

        for char in s:
            if char not in letter_dict:
                letter_dict[char] = 1
            else:
                letter_dict[char] += 1

        if len(letter_dict) == 1:
            return letter_dict[s[0]]

        res = 0
        odd = 0

        for i in letter_dict.values():
            if i > 1:
                if i % 2 == 0:
                    res += i
                else:
                    res += i - 1
                    odd += 1
            else:
                odd += 1

        if odd > 0:
            res += 1

        return res

if __name__ == "__main__":
    obj = Solution()
    s = "abccccddd"
    print(obj.longestPalindrome(s))