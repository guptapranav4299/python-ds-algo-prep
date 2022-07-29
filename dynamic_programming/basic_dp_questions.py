
global memo
count = 0

def fibonacci_memoization(n):
    global count
    count += 1
    if n <= 2:
        return 1
    # memoization part
    if memo[n] != -1:
        return memo[n]
    # recursive part
    memo[n] = fibonacci_memoization(n - 1) + fibonacci_memoization(n - 2)
    return memo[n]

def fibonacci_tabular(n):
    fib = [-1 for i in range(n+1)]
    fib[1] = fib[2] = 1
    for i in range(3,n+1):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[n]

"""
You are given a positive integer N . You have to reduce it by performing below operations:
1. reduce it to n - 1
2. if it is divisible by 2 then divide by 2
3. if it is divisible by 3 then divide 3
Find min operations
"""

def reduce_n_greedy(n):
    operations = 0
    while n >1:
        if n % 3 == 0:
            n = n // 3
            operations += 1
        elif n % 2 == 0:
            n = n // 2
            operations += 1
        else:
            n = n - 1
            operations += 1

    return operations

def reduce_n_greedy_recursive(n):
    if n == 1:
        return 0
    ans = 10000001
    if n % 2 == 0:
        ans = min(ans, reduce_n_greedy_recursive(n //2))
    if n % 3 == 0:
        ans = min(ans, reduce_n_greedy_recursive(n//3))
    ans = min(ans, reduce_n_greedy_recursive(n - 1))
    ans += 1

    return ans

# global dp
# def reduce_n_greedy_dp_memoize(n):
#     if n == 1:
#         return 0
#     ans = 10000001
#     if n % 2 == 0:
#         ans = min(ans, reduce_n_greedy_recursive(n //2))
#     if n % 3 == 0:
#         ans = min(ans, reduce_n_greedy_recursive(n//3))
#     ans = min(ans, reduce_n_greedy_recursive(n - 1))
#     ans += 1
#
#     return ans

if __name__ == "__main__":
    n = 100
    # memo = [-1 for i in range(n+1)]
    # print("Fibonacci number----->",fibonacci_memoization(n))
    # print("Function Calls---->",count)
    # print(fibonacci_tabular(n))
    # print(reduce_n_greedy(10))
    print(reduce_n_greedy_recursive(10))
    dp = [-1 for i in range(n + 1)]
