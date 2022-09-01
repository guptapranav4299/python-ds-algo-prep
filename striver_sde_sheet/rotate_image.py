"""
48. Rotate Image

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]


Constraints:

    n == matrix.length == matrix[i].length
    1 <= n <= 20
    -1000 <= matrix[i][j] <= 1000

"""
from typing import List


class Solution:
    """
    Approach - 1
     We transpose the matrix and then reverse each row, and since we are making changes in the matrix
     itself space complexity gets reduced to O(1).
     Time - 0(n ^ 2)
     space - 0(1)
    """
    def rotate_2(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(n):
            for j in range(n //2):
                temp = matrix[i][j]
                matrix[i][j], matrix[i][n - 1 - j] = matrix[i][n - 1 - j], matrix[i][j]


    """
    Best Solution
    Approach - 2
    move elements from bottom left in clockwise direction and storing the first element in a variable.
    time - 0(n^2)
    space - 0(1)
    """
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix) - 1

        while l < r:
            for i in range(r - l):
                top, bottom = l, r

                # save the topleft item
                top_left = matrix[top][l + i]

                # move bottom left to top left
                matrix[top][l + i] = matrix[bottom - i][l]

                # move bottom right to bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # move top right to bottom right
                matrix[bottom][r - i] = matrix[top + i][r]

                # move top left to move top right
                matrix[top + i][r] = top_left

            r -= 1
            l += 1


if __name__ == "__main__":
    obj = Solution()
    mat = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    mat2 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    obj.rotate(mat)
    print(mat)
    print("------------------------------")
    obj.rotate(mat2)
    print(mat2)
