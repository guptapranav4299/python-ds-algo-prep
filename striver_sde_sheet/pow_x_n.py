"""
50. Pow(x, n)

Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000

Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100

Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25



Constraints:

    -100.0 < x < 100.0
    -231 <= n <= 231-1
    -104 <= xn <= 104


"""

class Solution:
    def brute_force(self, x, n):
        ans = 1.0
        for i in range(1, n+1):
            ans *= x

        return ans

    def recursive_approach(self, x, N):
        if N == 0:
            return 1.0
        y = self.recursive_approach(x, N // 2)
        if N % 2 == 0:
            return y * y
        else:
            return y * y * x

    def iterative_approach(self, x, n):
        isNegative = False
        if n < 0:
            isNegative = True

        ans = 1
        n = abs(n)

        while n > 0:
            if n % 2 == 0:
                x = x * x
                n = n // 2
            else:
                ans = ans * x
                n -= 1

        if isNegative:
            return 1 / ans
        else:
            return ans


if __name__ == "__main__":
    obj = Solution()
    x = 2.000
    n = -2
    if n >= 0:
        print(obj.brute_force(x, n))
    else:
        print(1.0/(obj.brute_force(x, -n)))
    if n >= 0:
        print(obj.recursive_approach(x, n))
    else:
        print(1.0/obj.recursive_approach(x, -n))

    print(obj.iterative_approach(x,n))
