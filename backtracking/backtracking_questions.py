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


if __name__ == "__main__":
    # obj = BackTrackingQuestions()
    # arr = ['a', 'b', 'c']
    # print(obj.find_subsets(arr))

    obj2 = nQueens()
    n = 4
    rows, cols = (n, n)
    board = [[0 for i in range(cols)] for j in range(rows)]
    # print(obj2.check_nQueens(board, n, 0))
    # print(obj2.count_no_ways_nQueens(board, n, 0))
    obj2.print_all_nQueens(board, n, 0)
