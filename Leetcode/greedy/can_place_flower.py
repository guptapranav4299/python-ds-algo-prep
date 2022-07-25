"""
605. Can Place Flowers

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

Constraints:

    1 <= flowerbed.length <= 2 * 104
    flowerbed[i] is 0 or 1.
    There are no two adjacent flowers in flowerbed.
    0 <= n <= flowerbed.length
"""

from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        #   Logic is simple at each index we check currnt position, prev and next position
        #   if it contains "1" continue to next iteratinon
        #   else increase count
        #   if n is less than or equal to count , return True
        helper = [0] + flowerbed + [0]
        count = 0
        for i in range(1, len(helper) - 1):
            if helper[i] == 1 or helper[i - 1] == 1 or helper[i + 1] == 1:
                continue
            else:
                count += 1
                helper[i] = 1
        return count >= n
