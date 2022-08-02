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


if __name__ == "__main__":
    obj = Solution()
    arr = [2, 7, 4, 5, 19]
    given_sum = 12
    print(obj.subset_problem_brute_force(arr, given_sum))