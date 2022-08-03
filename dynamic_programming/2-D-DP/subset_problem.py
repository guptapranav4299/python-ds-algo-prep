"""
Given sum and an array of non negative numbers. Determine if subset of array exists if sum of subsets
equal to the given sum.

arr = [1,2,3,4]
sum = 6
"""


from itertools import combinations


class Solution:
    @classmethod
    def subset_problem_brute_force(cls, arr, given_sum):
        comb = []
        for i in range(len(arr) + 1):
            comb += [list(j) for j in combinations(arr, i)]

        for ls in comb:
            if sum(ls) == given_sum:
                return True

        return False

    @classmethod
    def subset_problem_recursive(cls, arr, index, given_sum):
        if index == -1:
            return given_sum == 0

        ans = False

        # include arr[x]
        if given_sum >= arr[index]:
            ans |= cls.subset_problem_recursive(arr, index - 1, given_sum - arr[index])

        # exclude arr[x]
        ans |= cls.subset_problem_recursive(arr, index - 1, given_sum)

        return ans

    # time - o(index*sum)
    @classmethod
    def subset_problem_memoization(cls, memo, arr, index, given_sum):
        if index == -1:
            return given_sum == 0

        if memo[index][given_sum] != -1:
            return memo[index][given_sum]

        ans = False

        # include arr[x]
        if given_sum >= arr[index]:
            ans |= cls.subset_problem_memoization(memo, arr, index - 1, given_sum - arr[index])

        # exclude arr[x]
        ans |= cls.subset_problem_memoization(memo, arr, index - 1, given_sum)

        memo[index][given_sum] = ans
        # print(memo)
        return memo[index][given_sum]

    # Time - 0(index * sum)
    # Space - 0(index * sum)
    @classmethod
    def subset_problem_tabulation(cls,table, arr, index, given_sum):
        n = len(arr)
        for i in range(n + 1):
            table[i][0] = True

        for i in range(1,n + 1):
            table[0][i] = False

        for i in range(1, n + 1):
            for j in range(1, given_sum + 1):
                if j < arr[i - 1]:
                    table[i][j] = table[i-1][j]
                if j >= arr[i - 1]:
                    table[i][j] = table[i-1][j] or table[i - 1][j - arr[i -1]]

        return table[n][given_sum]

    # time - o (index * sum)
    # space - -o (2* sum)
    @classmethod
    def subset_problem_tabulation_space_optimised_l1(cls,table, arr, index, given_sum):
        n = len(arr)
        # for i in range(n + 1):
        #     table[i][0] = True
        table[0][0] = True

        for i in range(1,n + 1):
            table[0][i] = False

        for i in range(1, n+1):
            for j in range(given_sum+1):
                table[1][j] = table[0][j]

                if j - arr[i - 1] > 0:
                    table[1][j] |= table[0][j - arr[i]]

            for j in range(given_sum+1):
                table[0][j] = table[1][j]

        return table[1][given_sum]

    # time - o(index * sum)
    # space - o(sum)
    @classmethod
    def subset_problem_tabulation_space_optimised_l2(cls,table, arr, index, given_sum):
        n = len(arr)
        table[0] = True

        for i in range(1,n + 1):
            table[i] = False

        for i in range(1, n+1):
            for j in range(given_sum, -1, -1):
                if j - arr[i - 1] > 0:
                    table[j] |= table[j - arr[i]]

        return table[given_sum]


if __name__ == "__main__":
    obj = Solution()
    arr = [2, 7, 4, 5, 19]
    given_sum = 12

    print(obj.subset_problem_brute_force(arr, given_sum))
    print(obj.subset_problem_recursive(arr,len(arr) - 1,given_sum))

    memo = [[-1 for i in range(given_sum + 1)] for j in range(len(arr))]
    print(obj.subset_problem_memoization(memo, arr, len(arr) - 1, given_sum))

    table = [[False for i in range(given_sum + 1) ] for j in range(len(arr) + 1)]
    print(obj.subset_problem_tabulation(table, arr, len(arr) - 1, given_sum))

    table_space = [[False for i in range(given_sum + 1)] for j in range(2)]
    print(obj.subset_problem_tabulation_space_optimised_l1(table_space, arr, len(arr) - 1, given_sum))

    table_n = [False for i in range(given_sum + 1)]
    print(obj.subset_problem_tabulation_space_optimised_l2(table_n, arr, len(arr) - 1, given_sum))
