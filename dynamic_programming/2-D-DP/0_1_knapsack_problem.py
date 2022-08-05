"""
The famous knapsack problem. You are packing for a vacation on the sea side and you are going to carry
only one bag with capacity S (1 <= S <= 2000). You also have N (1<= N <= 2000) items that you might want
to take with you to the sea side. Unfortunately you can not fit all of them in the knapsack so you will
have to choose.For each item you are given its size and its value. You want to maximize the total value
of all the items you are going to bring. What is this maximum total value?

Input
On the first line you are given S and N. N lines follow with two integers on each line describing one of your
items. The first number is the size of the item and the next is the value of the item.

Output
You should output a single integer on one like - the total maximum value from the best choice of items
for your trip.

Example

Input:
4 5
1 8
2 4
3 0
2 5
2 3


Output:
13

"""


class Solution:
    @classmethod
    def knapsack_recursive(cls, size_arr, val_arr, index , cap):
        if index == 0 or cap == 0:
            return 0

        ans = 0
        # If weight of the nth item is
        # more than Knapsack of capacity W,
        # then this item cannot be included
        # in the optimal solution
        if size_arr[index] <= cap:
            ans = val_arr[index] + cls.knapsack_recursive(size_arr, val_arr, index - 1, cap - size_arr[index])

        # return the maximum of two cases:
        # (1) nth item included
        # (2) not included
        ans = max(ans, cls.knapsack_recursive(size_arr, val_arr, index - 1, cap))

        return ans

    @classmethod
    def knapsack_memoization(cls, memo, size_arr, val_arr, index, cap):
        if index == 0 or cap == 0:
            return 0
        if memo[index][cap] != -1:
            return memo[index][cap]

        ans = 0
        if size_arr[index] <= cap:
            ans = val_arr[index] + cls.knapsack_recursive(size_arr, val_arr, index - 1, cap - size_arr[index])

        ans = max(ans, cls.knapsack_recursive(size_arr, val_arr, index - 1, cap))
        memo[index][cap] = ans
        return memo[index][cap]


if __name__ == "__main__":
    obj = Solution()
    n = 3
    cap = 50
    size_arr = [10, 20, 30]
    val_arr = [60, 100, 120]
    print(obj.knapsack_recursive(size_arr,val_arr,n - 1,cap))

    memo = [[-1 for i in range(cap + 1)] for j in range(n)]
    print(obj.knapsack_memoization(memo, size_arr,val_arr,n - 1,cap))
