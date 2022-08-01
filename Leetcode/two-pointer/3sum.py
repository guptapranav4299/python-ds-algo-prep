"""
15. 3-Sum
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

Constraints:

    3 <= nums.length <= 3000
    -105 <= nums[i] <= 105


"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        ans = []
        nums.sort()

        for i in range(len(nums)):

            # i is at our first pointer call it 'A'
            # if value at A is repeating we need to skip it as we don't want permutaions in our answer
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            else:
                # searching for next two pointer, let's call them B and C
                # such that -> A + B + C = 0 or B + C == -A (as question requires)
                # search range for B start from i+1 and ends just before the index of pointer C
                # and for C it starts from last index of nums array and ends just before pointer B
                # intitially these are the values from where our search starts
                rem = -1 * nums[i]
                p1 = i + 1
                p2 = len(nums) - 1

                # now the search starts
                while p1 < p2:
                    # print("Deep", p1, p2)
                    if nums[p1] + nums[p2] < rem:
                        p1 += 1
                    elif nums[p1] + nums[p2] > rem:
                        p2 -= 1
                    else:
                        # Values of A, B, C are satisfying the condition: A + B + C = 0 OR B + C = -A
                        ans.append([nums[i], nums[p1], nums[p2]])
                        # print(ans)

                        """
                        #Edge Case 1: 

                        [6, 0 2, 3, 3, 3, 3, 9]
                         A       B        C

                        As values at B and C are same and they will remain same for all next iterations
                        for current pointer A=6, in that case we will be adding same values multiple times 
                        in ans array which is not allowed in question, so we better move to next value of
                        pointer A, this can be done by breaking while loop
                        """

                        if nums[p1] == nums[p2]:
                            break
                        else:
                            x, y = nums[p1], nums[p2]
                            while nums[p1] == x:
                                p1 += 1
                            while nums[p2] == y:
                                p2 -= 1

                        """
                        # Edge Case 2: if values of B and/or C are repeating, 
                        again we don't want permutation or repeating values in our answer 
                        so we better move our pointer B and C till the point where repeatation stops
                        """

        return ans


if __name__ == "__main__":
    obj = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    print(obj.threeSum(nums))