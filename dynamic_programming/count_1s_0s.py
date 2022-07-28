#  No. of ways to fill an array with 1s and 0s such that there are no consecutive 1s


def ways_array_recursive(index, n, previous_case):
    if index == n + 1:
        return 1
    ans = 0
    # place 0 here
    ans += ways_array_recursive(index + 1, n, False)
    # place 1 here
    if not previous_case:
        ans += ways_array_recursive(index + 1, n, True)

    return ans


if __name__ == "__main__":
    n = 3
    print(ways_array_recursive(1, n, False))
