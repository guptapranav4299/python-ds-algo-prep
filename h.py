class Solution:
    def findNth(self, n):
        def helper(n):
            if n == 0:
                return 0
            if n == 1:
                return 1
            if n == 2:
                return 1 % (pow(10, 9) + 7)
            fib = [-1 for i in range(n + 1)]
            fib[0] = 0
            fib[1] = 1
            for i in range(2, n + 1):
                if i % 5 == 0:
                    fib[i] = 11
                else:
                    fib[i] = (fib[i - 1] + fib[i - 2]) % (pow(10,9) + 7)

            return fib[n]
        ans = helper(n)
        return ans


obj = Solution()
print(obj.findNth(6621))