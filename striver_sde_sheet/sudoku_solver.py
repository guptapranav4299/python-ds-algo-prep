"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

    Each of the digits 1-9 must occur exactly once in each row.
    Each of the digits 1-9 must occur exactly once in each column.
    Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.

The '.' character indicates empty cells.

Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]]
Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],
["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],
["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],
["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],
["3","4","5","2","8","6","1","7","9"]]
Explanation: The input board is shown above and the only valid solution is shown below:

Constraints:

    board.length == 9
    board[i].length == 9
    board[i][j] is a digit or '.'.
    It is guaranteed that the input board has only one solution.

"""


from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def isSafe(i, j, num, n):
            for k in range(n):
                if board[i][k] == str(num) or board[k][j] == str(num):
                    return False

            sx, sy = (i // 3) * 3, (j // 3) * 3

            for x in range(sx, sx + 3):
                for y in range(sy, sy + 3):
                    if board[x][y] == str(num):
                        return False

            return True

        def sudokuSolver(i, j, n):
            nonlocal res

            if i == n:
                res = copy.deepcopy(board)
                return

            if j == n:
                return sudokuSolver(i + 1, 0, n)

            if board[i][j] != ".":
                return sudokuSolver(i, j + 1, n)

            for num in range(1, n + 1):
                if isSafe(i, j, num, n):
                    board[i][j] = str(num)

                    if sudokuSolver(i, j + 1, n):
                        return True

                board[i][j] = "."

            return False

        res = None

        sudokuSolver(0, 0, len(board))

        board[::] = res