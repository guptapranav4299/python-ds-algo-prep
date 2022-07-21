
class BackTracking:
    @classmethod
    def array_backtracking(cls,arr, idx, n, val):
        # base case
        if idx == n:
            print(arr)
            return
        # recursive case
        arr[idx] = val
        cls.array_backtracking(arr, idx+1, n, val+1)
        # backtrack case
        arr[idx] = -1 * arr[idx]

if __name__ == "__main__":
    obj = BackTracking()
    a = [0] * 5
    obj.array_backtracking(a, 0, len(a), 1)
    print("--------After Backtracking-------------")
    print(a)
