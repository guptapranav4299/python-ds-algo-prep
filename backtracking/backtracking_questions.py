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


if __name__ == "__main__":
    obj = BackTrackingQuestions()
    arr = ['a', 'b', 'c']
    print(obj.find_subsets(arr))
