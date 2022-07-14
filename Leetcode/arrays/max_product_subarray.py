from typing import List
import sys

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        try:
            currentProduct = 1
            max_num = -sys.maxsize - 1
            for i in range(0,len(nums)):
                currentProduct *= nums[i]
                max_num = max(max_num,currentProduct)
                if currentProduct == 0:
                    currentProduct = 1

            currentProduct = 1
            for i in range(len(nums) -1, -1,-1):
                currentProduct *= nums[i]
                max_num = max(max_num,currentProduct)
                if currentProduct == 0:
                    currentProduct = 1

            return max_num

        except Exception as e:
            raise Exception("Error in max product---->",str(e))