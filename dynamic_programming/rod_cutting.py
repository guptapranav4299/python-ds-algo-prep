INT_MIN = -32767


# time complexitiy = 0(n ^2) space complexity - o(2^n)
def rod_cutting_recursive(prices, n):
    if n == 0:
        return 0
    ans = 0
    for i in range(0, n):
        ans = max(ans, prices[i] + rod_cutting_recursive(prices, n - i - 1))
    return ans


# time complexitiy = 0(n ^2) space complexity - o(n)
def rod_cutting_memoization(prices, n, memo):
    if n == 0:
        return 0
    if memo[n] != 0:
        return memo[n]
    ans = 0
    for i in range(0, n):
        ans = max(ans, prices[i] + rod_cutting_recursive(prices, n - i - 1))
    memo[n] = ans
    return memo[n]


# time complexitiy = 0(n ^2) space complexity - o(n)
def rod_cutting_tabular(prices, n):
    val = [0 for i in range(n + 1)]
    val[0] = 0
    for i in range(1, n + 1):
        max_val = INT_MIN
        for j in range(i):
            max_val = max(max_val, prices[j] + val[i - j - 1])
        val[i] = max_val

    return val[n]


if __name__ == "__main__":
    prices = [1, 3, 4, 5, 7, 9, 10, 11]
    n = 8
    print(rod_cutting_recursive(prices, n))
    memo = [0 for i in range(100001)]
    print(rod_cutting_memoization(prices, n, memo))
    print(rod_cutting_tabular(prices, n))
