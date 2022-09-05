"""
Problem - 1
Zonal Computing Olympiad 2014, 30 Nov 2013

In ICO School, all students have to participate regularly in SUPW. There is a different SUPW activity
each day, and each activity has its own duration. The SUPW schedule for the next term has been announced, including information about the number of minutes taken by each activity.

Nikhil has been designated SUPW coordinator. His task is to assign SUPW duties to students, including
himself. The school's rules say that no student can go three days in a row without any SUPW duty.

Nikhil wants to find an assignment of SUPW duty for himself that minimizes the number of minutes he
spends overall on SUPW.

Input format

Line 1: A single integer N, the number of days in the future for which SUPW data is available.

Line 2: N non-negative integers, where the integer in position i represents the number of minutes
required for SUPW work on day i.

Output format

The output consists of a single non-negative integer, the minimum number of minutes that Nikhil
needs to spend on SUPW duties this term

Sample Input 1

10
3 2 1 1 2 3 1 3 2 1


Sample Output 1

4


(Explanation: 1+1+1+1)

Sample Input 2

8
3 2 3 2 3 5 1 3


Sample Output 2

5


(Explanation: 2+2+1)

Test data

There is only one subtask worth 100 marks. In all inputs:

• 1 ≤ N ≤ 2×105

• The number of minutes of SUPW each day is between 0 and 104, inclusive.


"""


"""
Problem 2
Zonal Computing Olympiad 2014, 30 Nov 2013

In IPL 2025, the amount that each player is paid varies from match to match. The match fee depends on the quality of opposition, the venue etc.

The match fees for each match in the new season have been announced in advance. Each team has to enforce a mandatory rotation policy so that no player ever plays three matches in a row during the season.

Nikhil is the captain and chooses the team for each match. He wants to allocate a playing schedule for himself to maximize his earnings through match fees during the season.

Input format

Line 1: A single integer N, the number of games in the IPL season.

Line 2: N non-negative integers, where the integer in position i represents the fee for match i.

Output format

The output consists of a single non-negative integer, the maximum amount of money that Nikhil can earn during this IPL season.

Sample Input 1

5 
10 3 5 7 3 


Sample Output 1

23


(Explanation: 10+3+7+3)

Sample Input 2

8
3 2 3 2 3 5 1 3


Sample Output 2

17


(Explanation: 3+3+3+5+3)

Test data

There is only one subtask worth 100 marks. In all inputs:

    • 1 ≤ N ≤ 2×105

    • The fee for each match is between 0 and 104, inclusive.


Live evaluation data

There are 12 test inputs on the server during the exam.
"""


class SUPW:
    @classmethod
    def min_assignments_dp_tabular(cls, arr, n):
        dp = [-1 for i in range(n)]
        dp[0] = arr[0]
        dp[1] = arr[1]
        dp[2] = arr[2]

        for i in range(3, n):
            dp[i] = min([dp[i - 1], dp[i - 2], dp[i - 3]]) + arr[i]
        return min([dp[n - 1], dp[n - 2], dp[n - 3]])


if __name__ == "__main__":
    obj = SUPW()
    n = 10
    arr = [3,2,1,1,2,3,1,3,2,1]
    supw = obj.min_assignments_dp_tabular(arr, n)
    print(supw)
    ipl_solution = sum(arr) - supw
    print(ipl_solution)