"""
1. In place algo
2. Unstable algo
3. O(n2) complexity
4. Approach - Find min element and place it in the first  index, then find second min element and place to
to 2nd index.
5. Optimal where we need less memory writes.
"""

class SelectionSort:
    @classmethod
    def selection_sort(cls, arr):
        try:
            n = len(arr)
            for i in range(n-1):
                min_idx = i
                for j in range(i+1, n):
                    if arr[j] < arr[min_idx]:
                        min_idx = j

                arr[min_idx], arr[i] = arr[i], arr[min_idx]
            return arr
        except Exception as e:
            raise Exception("Error in selection sort---->",str(e))

    @classmethod
    def reverse_selection_sort(cls,arr):
        try:
            n = len(arr)
            for i in range(n-1):
                max_idx = i
                for j in range(i+1, n):
                    if arr[j] > arr[max_idx]:
                        max_idx = j
                arr[max_idx], arr[i] = arr[i], arr[max_idx]

            return arr
        except Exception as e:
            raise Exception("Error in reverse selection sort---->",str(e))


if __name__ == "__main__":
    obj = SelectionSort()
    a = [5, 4, 6, 1, 0, 9]
    print(obj.selection_sort(a))
    print(obj.reverse_selection_sort(a))
