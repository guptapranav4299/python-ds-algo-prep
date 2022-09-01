"""
73. Set Matrix Zeroes

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

Constraints:

    m == matrix.length
    n == matrix[0].length
    1 <= m, n <= 200
    -231 <= matrix[i][j] <= 231 - 1



Follow up:

    A straightforward solution using O(mn) space is probably a bad idea.
    A simple improvement uses O(m + n) space, but still not the best solution.
    Could you devise a constant space solution?

"""
import copy
from typing import List


class Solutions:
    """
    Approach - 1
    Make a copy of the matrix and modifu the values in the old matrix using state of the copied
    matrix.
    Time - 0(m*n)
    Space - 0(m*m*n)
    """
    def brute_force(self, matrix):
        temp_matrix = copy.deepcopy(matrix)
        a = len(temp_matrix)
        b = len(temp_matrix[0])
        for i in range(a):
            for j in range(b):
                if temp_matrix[i][j] == 0:
                    matrix[i] = [0] * b
                    for k in range(a):
                        matrix[k][j] = 0
    """
    Approach - 2 
    Make 2 lists for row and column. Mark which row to make 0 after iterating the matrix.
    Then make matrix zero according to the index.
    Time - o(m*n)
    Space - o(m + n)
    """
    def space_efficient_better(self, matrix):
        check_row = set()
        check_column = set()
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    check_row.add(i)
                    check_column.add(j)

        for i in range(m):
            if i in check_row:
                matrix[i] = [0] * n
                continue

            for j in range(n):
                if j in check_column:
                    matrix[i][j] = 0

    """
    Aprroach - 3
    Instead of using separate row and col array we can mark 0 on the first row and column after
    iterating to them. For matrix[0][0] element we can use a boolean variable. if bool is True then
    we need to make rows 0 else leave the row as it is.
    Time - 0(m * n)
    Space - 0(1)
    """
    def best_solution(self, matrix):
        rows, cols = len(matrix), len(matrix[0])
        row_zero = False
        # checking matrix value
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    # checking if first element is 0 or not
                    if i > 0:
                        matrix[i][0] = 0
                    else:
                        row_zero = True

        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for i in range(rows):
                matrix[i][0] = 0

        if row_zero:
            for j in range(cols):
                matrix[0][j] = 0


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        row_zero = False
        # checking matrix value
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    # checking if first element is 0 or not
                    if i > 0:
                        matrix[i][0] = 0
                    else:
                        row_zero = True

        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for i in range(rows):
                matrix[i][0] = 0

        if row_zero:
            for j in range(cols):
                matrix[0][j] = 0


if __name__ == "__main__":
    obj = Solutions()
    obj2 = Solution()
    mat = [[1,1,1],[1,0,1],[1,1,1]]
    mat2 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    mat3 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    mat4 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    # obj.setZeroes(mat)
    obj.brute_force(mat2)
    print(mat2)
    print("-------------------")
    obj.space_efficient_better(mat3)
    print(mat3)
    print("-------------------")
    obj.best_solution(mat4)
    print(mat4)
    print("-------------------")
    mat5 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    obj2.setZeroes(mat5)
    print(mat5)

