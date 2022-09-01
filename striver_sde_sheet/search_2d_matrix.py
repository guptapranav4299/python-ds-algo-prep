"""
74. Search a 2D Matrix

Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix.
This matrix has the following properties:
Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

Constraints:

    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 100
    -104 <= matrix[i][j], target <= 104

"""
from typing import List


class Solution:

    def naive_approach(self, matrix, target):
        r = len(matrix)
        c = len(matrix[0])

        for i in range(r):
            for j in range(c):
                if matrix[i][j] == target:
                    return True

        return False

    """
    Comapre target row-wise with current and next row element, if it is between those 2 elements
    save row_number in a variable and then traverse through only that column and get the target element.
    
    Time - 0(row + col)
    Space - 0(1)
    """
    def searchMatrix_efficient(self, matrix: List[List[int]], target: int) -> bool:
        r = len(matrix)
        c = len(matrix[0])
        row_number = -1
        for i in range(r - 1):
            if target >= matrix[i][0] and target < matrix[i + 1][0]:
                row_number = i
            elif target >= matrix[i + 1][0]:
                row_number = i + 1
        for j in range(c):
            if target == matrix[row_number][j]:
                return True

        return False


if __name__ == "__main__":
    obj = Solution()
    mat = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 11
    print(obj.naive_approach(mat, target))
    print(obj.searchMatrix_efficient(mat, target))