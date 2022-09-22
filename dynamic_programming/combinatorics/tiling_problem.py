"""
Tiling Problem
Given a 2 X N board and tiles of size '2 X 1' , count the number of ways to tile the given board
using '2 X 1' tiles. A tile can be placed horizontally or vertically.

"""

class Solution:
    def recursive(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.recursive(n - 1) + self.recursive(n - 2)

    def recursive_tiling_2(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.recursive_tiling_2(n - 1) + 2 * self.recursive_tiling_2(n - 2)

    def tiling_4(self, n):
        f = [0 for i in range(n + 1)]
        g = [0 for i in range(n + 1)]

        f[0] = g[0] = 1
        f[1] = g[1] = 0
        for i in range(2, n + 1):
            f[i] = f[i - 2]+ 2*g[i - 2]
            g[i] = g[i - 2] + f[i]

        return f[n]

    
if __name__ == "__main__":
    obj = Solution()
    n = 2
    print(obj.recursive(n))
    print(obj.recursive_tiling_2(n))
    print(obj.tiling_4(n))