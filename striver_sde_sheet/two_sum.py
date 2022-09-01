"""
1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that
they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same
element twice.
You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:

    2 <= nums.length <= 104
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    Only one valid answer exists.

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""
import copy


class Solution:
    """
    Approach - 1
    We run 1 nested loops and check the target_sum.
    Time - 0(n * n)
    Space - 0(1)
    """
    def brute_approach(self, nums, target):
        n = len(nums)
        res = []
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    res.append(i)
                    res.append(j)
                    break

            if len(res) == 2:
                break

        return res

    """
    Approach - 2
    We make a duplicate array and sort that array first and then run 2 pointers start and end, check the sum if sum is greater
    than the target sum then we decrease end pointer and vice versa.
    Time - 0(nlogn)
    Space - 0(n)
    """
    def better_approach(self, nums, target):
        store, ans = [], []
        store = copy.deepcopy(nums)
        store = sorted(store)
        start, end = 0, len(store) - 1
        n1, n2 = -1, -1
        while start < end:
            if store[start] + store[end] == target:
                n1 = store[start]
                n2 = store[end]
                break
            elif store[start] + store[end] > target:
                end = end - 1
            else:
                start += 1

        ans.append(nums.index(n1))
        ans.append(nums.index(n2))
        return ans

    """
    Approach - 3
    We create a map to see if there exists a value target – x for each value x. If target – x is found 
    in the map, can return current element x’s index and (target-x)’s index
    Time - 0(n)
    Space - 0(n)
    """

    def efficient_approach(self, nums, target):
        hashmap = {}
        for index, value in enumerate(nums):
            difference = target - value
            if difference in hashmap:
                return [hashmap[difference], index]
            hashmap[value] = index
            print(hashmap)


if __name__ == "__main__":
    obj = Solution()
    nums = [3,2,4]
    target = 6
    print(obj.brute_approach(nums, target))
    print(obj.efficient_approach(nums, target))
    print(obj.better_approach(nums, target))
