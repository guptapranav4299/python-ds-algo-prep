
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


if __name__ == "__main__":
    n = 100
    # memo = [-1 for i in range(n+1)]
    # print("Fibonacci number----->",fibonacci_memoization(n))
    # print("Function Calls---->",count)

    print(fibonacci_tabular(n))