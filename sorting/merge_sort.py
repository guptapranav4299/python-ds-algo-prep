"""
1.Time - o(n logn)
2. Space o(n)
3. stable algo
4.
"""

class MergeSort:
    @classmethod
    def merge(cls, arr, low, mid, high):
        left = arr[low: mid + 1]
        right = arr[mid + 1: high + 1]
        i = 0
        j = 0
        k = low

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                k += 1
                i += 1
            else:
                arr[k] = right[j]
                k += 1
                j += 1
        while i < len(left):
            arr[k] = left[i]
            k += 1
            i += 1

        while j < len(right):
            arr[k] = right[j]
            k += 1
            j += 1

    @classmethod
    def merge_sort(cls, arr, low, high):
        if low < high:
            mid = (low + high) // 2
            cls.merge_sort(arr, low, mid)
            cls.merge_sort(arr, mid + 1, high)
            cls.merge(arr, low, mid, high)


if __name__ == "__main__":
    obj = MergeSort()
    arr = [10, 5, 30, 15, 7]
    obj.merge_sort(arr,0,len(arr) - 1)
    print("Sorted Array----->",arr)

