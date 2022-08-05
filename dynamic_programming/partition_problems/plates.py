"""
 Dr. Patel has N stacks of plates. Each stack contains K plates. Each plate has a positive beauty value, describing how beautiful it looks.

Dr. Patel would like to take exactly P plates to use for dinner tonight. If he would like to take a plate in a stack, he must also take all of the plates above it in that stack as well.

Help Dr. Patel pick the P plates that would maximize the total sum of beauty values.
Input

The first line of the input gives the number of test cases, T. T test cases follow. Each test case begins with a line containing the three integers N, K and P. Then, N lines follow. The i-th line contains K integers, describing the beauty values of each stack of plates from top to bottom.
Output

For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the maximum total sum of beauty values that Dr. Patel could pick.
Limits

Time limit: 20 seconds.
Memory limit: 1 GB.
1 ≤ T ≤ 100.
1 ≤ K ≤ 30.
1 ≤ P ≤ N * K.
The beauty values are between 1 and 100, inclusive.
Test Set 1

1 ≤ N ≤ 3.
Test Set 2

1 ≤ N ≤ 50.

SAMPLE INPUT
2
2 4 5
10 10 100 30
80 50 10 50
3 2 3
80 80
15 50
20 10

SAMPLE OUTPUT
Case #1: 250
Case #2: 180

n Sample Case #1, Dr. Patel needs to pick P = 5 plates:

    He can pick the top 3 plates from the first stack (10 + 10 + 100 = 120).
    He can pick the top 2 plates from the second stack (80 + 50 = 130) .

In total, the sum of beauty values is 250.

In Sample Case #2, Dr. Patel needs to pick P = 3 plates:

    He can pick the top 2 plates from the first stack (80 + 80 = 160).
    He can pick no plates from the second stack.
    He can pick the top plate from the third stack (20).

In total, the sum of beauty values is 180.
"""


def main():
    def recursion(ith_stack, plate_needed):

        # Base case for solving Recursion
        if (ith_stack >= N or plate_needed <= 0):
            return 0

        # Memoization
        # if value already present in the table so simply return that value
        if lookup_table[ith_stack][plate_needed]:
            return lookup_table[ith_stack][plate_needed]

        # Recursive function
        current_max = 0

        # if suppose plate needed > k then we have to choose minimum between plate_needed and k
        # Because when we have only 1 stack availble it has k = 5 but if our plate needed greater then k , then we have to choose minimum between the two values.
        for j in range(0, min(plate_needed, K) + 1):

            temp = recursion(ith_stack + 1, plate_needed - j)
            if j > 0:
                temp += plates_piles[ith_stack][j - 1]

            current_max = max(current_max, temp)

        lookup_table[ith_stack][plate_needed] = current_max
        return current_max

        # Choose no. of test cases

    T = int(input())

    # input
    # Number of stack = N
    # Number of plates per stack = K
    # Number of required plates = P
    for i in range(1, T + 1):
        N, K, P = [int(s) for s in input().split(" ")]

        # N,K,P
        '''
        N = number_of_stack 
        K = number_of_plates_per_stack 
        P = number_req_plates
        '''

        plates_piles = []

        # find the cummulative distribution of each stack
        for j in range(N):
            pile = []
            current = 0
            for s in input().split(" "):
                current += int(s)
                pile.append(current)
            plates_piles.append(pile)

        lookup_table = [[0] * (P + 1) for _ in range(N)]

        result = recursion(0, P)
        print("Case #{}: {}".format(i, result))


if __name__ == '__main__':
    main()