class BackTrackingQuestions:
    @classmethod
    def find_subsets(cls, nums):
        res = []
        subset = []

        def dfs(idx):
            if idx >= len(nums):
                res.append(subset.copy())
                return

            # include case
            subset.append(nums[idx])
            dfs(idx + 1)
            # not include case
            subset.pop()
            dfs(idx + 1)

        dfs(0)
        return res


class nQueens:
    @classmethod
    def check_nQueens(cls, board, n, col):
        if col >= n:
            print(board)
            return True

        for i in range(n):
            if cls.is_safe(board, n, i, col):
                board[i][col] = 1
                if cls.check_nQueens(board, n, col + 1):
                    return True
                board[i][col] = 0

        return False

    @classmethod
    def is_safe(cls, board, n, row, col):
        # column wise check
        for i in range(col):
            if board[row][i] == 1:
                return False

        # left diagnol wise check
        for i, j in zip(range(row, -1, -1),
                        range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        for i, j in zip(range(row, n, 1),
                        range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        return True

    @classmethod
    def count_no_ways_nQueens(cls, board, n, col):
        if col == n:
            return 1

        ways = 0
        for i in range(n):
            if cls.is_safe(board, n, i, col):
                board[i][col] = 1
                ways += cls.count_no_ways_nQueens(board, n, col + 1)
                board[i][col] = 0

        return ways

    @classmethod
    def print_all_nQueens(cls, board, n, col):
        if col == n:
            print(board)
            return

        for i in range(n):
            if cls.is_safe(board, n, i, col):
                board[i][col] = 1
                cls.print_all_nQueens(board, n, col + 1)
                board[i][col] = 0


class SudokuSolver:
    @classmethod
    def solveSudoku(cls, grid, i, j, n):
        if i == n:
            print(grid)
            return True
        if j == n:
            return cls.solveSudoku(grid, i + 1, 0, n)

        if grid[i][j] != 0:
            return cls.solveSudoku(grid, i, j + 1, n)

        for number in range(1, n + 1):
            if cls.isSafe(grid, i, j, number, n):
                grid[i][j] = number
                if cls.solveSudoku(grid, i, j, n):
                    return True

        grid[i][j] = 0
        return False

    @classmethod
    def isSafe(cls, grid, idx, idy, number, n):
        for k in range(n):
            if grid[k][idy] == number or grid[idx][k] == number:
                return False

        sx = (idx // 3) * 3
        sy = (idy // 3) * 3

        for x in range(sx, sx + 3):
            for y in range(sy, sy + 3):
                if grid[x][y] == number:
                    return False
        return True


class Rat_In_A_Maze:
    @classmethod
    def solve_maze(cls, maze):
        n = 4
        sol = [ [ 0 for j in range(4) ] for i in range(4) ]
        result = cls.solve_maze_rec(maze, 0, 0, n, sol)

        if not result:
            print("No solution exists")
        else:
            print("sol--->",sol)

    @classmethod
    def solve_maze_rec(cls, maze, idx, idy, n, sol):
        if idx == n - 1 and idy == n - 1 and maze[idx][idy] == 1:
            sol[idx][idy] = 1
            return True

        if cls.is_safe(maze, idx, idy, n):
            sol[idx][idy] = 1

            if cls.solve_maze_rec(maze, idx + 1, idy, n, sol):
                return True
            if cls.solve_maze_rec(maze, idx, idy + 1, n, sol):
                return True
            sol[idx][idy] = 0
            return False

    @classmethod
    def is_safe(cls, maze, x, y, n):
        if x >= 0 and y >= 0 and x < n and y < n and maze[x][y] == 1:
            return True
        else:
            return False


if __name__ == "__main__":
    # obj = BackTrackingQuestions()
    # arr = ['a', 'b', 'c']
    # print(obj.find_subsets(arr))

    # obj2 = nQueens()
    # n = 4
    # rows, cols = (n, n)
    # board = [[0 for i in range(cols)] for j in range(rows)]
    # # print(obj2.check_nQueens(board, n, 0))
    # # print(obj2.count_no_ways_nQueens(board, n, 0))
    # obj2.print_all_nQueens(board, n, 0)

    # obj3 = SudokuSolver()
    # # grid =[[0 for x in range(9)]for y in range(9)]
    # grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
    #         [5, 2, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 8, 7, 0, 0, 0, 0, 3, 1],
    #         [0, 0, 3, 0, 1, 0, 0, 8, 0],
    #         [9, 0, 0, 8, 6, 3, 0, 0, 5],
    #         [0, 5, 0, 0, 9, 0, 6, 0, 0],
    #         [1, 3, 0, 0, 0, 0, 2, 5, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 7, 4],
    #         [0, 0, 5, 2, 0, 6, 3, 0, 0]]
    #
    # print(obj3.solveSudoku(grid, 0, 0, 9))

    maze = [[1, 0, 0, 0],
            [1, 1, 0, 1],
            [0, 1, 0, 0],
            [1, 1, 1, 1]]
    obj4 = Rat_In_A_Maze()
    obj4.solve_maze(maze)
