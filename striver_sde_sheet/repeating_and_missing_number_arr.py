"""
https://www.geeksforgeeks.org/find-a-repeating-and-a-missing-number/

Repeat and Missing Number Array


There are certain problems which are asked in the interview to also check how you take care of
overflows in your problem.

This is one of those problems.

Please take extra care to make sure that you are type-casting your ints to long properly and at all places. Try to verify if your solution works if number of elements is as large as 105

    Food for thought :

        Even though it might not be required in this problem, in some cases,
        you might be required to order the operations cleverly so that the numbers do not overflow.
        For example, if you need to calculate n! / k! where n! is factorial(n),
        one approach is to calculate factorial(n), factorial(k) and then divide them.
        Another approach is to only multiple numbers from k + 1 ... n to calculate the result.
        Obviously approach 1 is more susceptible to overflows.

You are given a read only array of n integers from 1 to n.

Each integer appears exactly once except A which appears twice and B which is missing.

Return A and B.

Note: Your algorithm should have a linear runtime complexity. Could you implement it
without using extra memory?

Note that in your output A should precede B.

Example:

Input:[3 1 2 5 3]

Output:[3, 4]

A = 3, B = 4


"""

class Solution:

    def brute_force(self, nums):
        mp ={}
        ans = []
        for i in nums:
            if i not in mp:
                mp[i] = 1
            else:
                mp[i] += 1

        sum1 = 0
        for k,v in mp.items():
            if v > 1:
               ans.append(k)
            sum1 += k
        n = len(nums)
        sum2 = (n*(n+1))//2
        ans.append(sum2 - sum1)
        return ans

    def optimal(self, arr, n):

        global x, y
        x = 0
        y = 0

        # Will hold xor of all elements
        # and numbers from 1 to n
        xor1 = arr[0]

        # Get the xor of all array elements
        for i in range(1, n):
            xor1 = xor1 ^ arr[i]

        # XOR the previous result with numbers
        # from 1 to n
        for i in range(1, n + 1):
            xor1 = xor1 ^ i

        # Will have only single set bit of xor1
        set_bit_no = xor1 & ~(xor1 - 1)

        # Now divide elements into two
        # sets by comparing a rightmost set
        # bit of xor1 with the bit at the same
        # position in each element. Also,
        # get XORs of two sets. The two
        # XORs are the output elements.
        # The following two for loops
        # serve the purpose
        for i in range(n):
            if (arr[i] & set_bit_no) != 0:

                # arr[i] belongs to first set
                x = x ^ arr[i]
            else:

                # arr[i] belongs to second set
                y = y ^ arr[i]

        for i in range(1, n + 1):
            if (i & set_bit_no) != 0:

                # i belongs to first set
                x = x ^ i
            else:

                # i belongs to second set
                y = y ^ i


        return [x,y]


if __name__ == "__main__":
    obj = Solution()
    nums = [3,1,2,3,5]
    print(obj.brute_force(nums))
    print(obj.optimal(nums, len(nums)))
