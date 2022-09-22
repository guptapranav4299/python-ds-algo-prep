"""
51. N-Queens

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no
two queens attack each other.
Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the
answer in any order.
Each solution contains a distinct board configuration of the n-queens' placement, where 'Q'
and '.' both indicate a queen and an empty space, respectively.

Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

Input: n = 1
Output: [["Q"]]

Constraints:

    1 <= n <= 9
"""


from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for i in range(n)]
        ans = []

        def queen(col, ans, lowerDiagonal, upperDiagonal, board, leftRow):

            if col == n:
                ans.append(["".join(r) for r in board])
                return
            for row in range(n):
                if leftRow[row] == 0 and lowerDiagonal[row + col] == 0 and upperDiagonal[n - 1 + col - row] == 0:
                    board[row][col] = "Q"
                    leftRow[row] = 1
                    lowerDiagonal[row + col] = 1
                    upperDiagonal[n - 1 + col - row] = 1
                    queen(col + 1, ans, lowerDiagonal, upperDiagonal, board, leftRow)
                    board[row][col] = "."
                    leftRow[row] = 0
                    lowerDiagonal[row + col] = 0
                    upperDiagonal[n - 1 + col - row] = 0

        queen(0, ans, [0] * (2 * n - 1), [0] * (2 * n - 1), board, [0] * n)
        return ans