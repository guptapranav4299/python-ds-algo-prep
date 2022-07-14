"""
1. Basic comparison algo
2. Inplace
3. o(n2) time complexity
"""

class BubbleSort:
    @classmethod
    def bubble_sort(cls, arr):
        try:
            n = len(arr)
            for i in range(n - 1):
                for j in range(n - i - 1):
                    if arr[j] > arr[j + 1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]

            return arr
        except Exception as e:
            raise Exception("Error in bubble sort---->", str(e))

    @classmethod
    def reverse_bubble_sort(cls, arr):
        try:
            n = len(arr)
            for i in range(n - 1):
                for j in range(n - i - 1):
                    if arr[j] < arr[j + 1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]

            return arr
        except Exception as e:
            raise Exception("Error in reverse bubble sort--->", str(e))


if __name__ == '__main__':
    obj = BubbleSort()
    a = [7, 6, 1, 2, 3, 9]
    print(obj.bubble_sort(a))
    print(obj.reverse_bubble_sort(a))
