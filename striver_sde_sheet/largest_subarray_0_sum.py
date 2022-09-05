"""
Largest subarray with 0 sum

Given an array having both positive and negative integers. The task is to compute the length of the largest subarray with sum 0.

Example 1:

Input:
N = 8
A[] = {15,-2,2,-8,1,7,10,23}
Output: 5
Explanation: The largest subarray with
sum 0 will be -2 2 -8 1 7.

Your Task:
You just have to complete the function maxLen() which takes two arguments an array A and n, where n is the size of the array A and returns the length of the largest subarray with 0 sum.

Expected Time Complexity: O(N*log(N)).
Expected Auxiliary Space: O(N).

Constraints:
1 <= N <= 105
-1000 <= A[i] <= 1000, for each valid i

"""


class Solution:
    def maxLen(self, n, arr):
        #Code here
        d = {0 : -1}
        curr_sum = 0
        ans = 0
        for i in range(len(arr)):
            curr_sum += arr[i]
            if curr_sum in d :
                ans = max(ans , i - d[curr_sum])
            else:
                d[curr_sum] = i
        return ans
