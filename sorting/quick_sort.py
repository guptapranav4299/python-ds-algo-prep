"""
1. Divide and Conquer ALgo
2. Time Complexity : o(n^2)
3. It is considered better because
    a. In place
    b. Cache Friendly
    c. Avg Case is o(nlogn)
    d. Tail Recursive
4. Partition is key function (Naive,
"""


class QuickSort:
    @classmethod
    def quick_sort_loumto_partition(cls, arr, low, high):
        if low < high:
            pivot = obj2.lomuto_partition(arr, low, high)
            cls.quick_sort_loumto_partition(arr, low, pivot - 1)
            cls.quick_sort_loumto_partition(arr, pivot + 1, high)

    @classmethod
    def quick_sort_hoarse_partition(cls, arr, low, high):
        if low < high:
            pivot = obj2.hoarse_partition(arr, low, high)
            cls.quick_sort_hoarse_partition(arr, low, pivot)
            cls.quick_sort_hoarse_partition(arr, pivot + 1, high)


class Partitions:
    # time- o(n) space - o(n)
    @classmethod
    def naive_partition(cls, arr, pivot):
        n = len(arr)
        arr[pivot], arr[n - 1] = arr[n - 1], arr[pivot]
        temp = []
        i = 0
        for counter in arr:
            if counter <= arr[n - 1]:
                temp.append(counter)

        for x in arr:
            if x > arr[n - 1]:
                temp.append(x)

        for i in range(len(arr)):
            arr[i] = temp[i]

    @classmethod
    def lomuto_partition(cls, arr, low, high):
        pivot = arr[high]
        i = low - 1
        for counter in range(low,high):
            if arr[counter] < pivot:
                i += 1
                arr[i],arr[counter] = arr[counter],arr[i]
        arr[i+1],arr[high] = arr[high],arr[i+1]
        return i+1

    @classmethod
    def hoarse_partition(cls, arr, low, high):
        pivot = arr[low]
        i = low - 1
        j = high + 1
        while True:
            i += 1
            while arr[i] < pivot:
                i+=1
            j -= 1
            while arr[j] > pivot:
                j-=1
            if i >= j:
                return j
            arr[i], arr[j] = arr[j], arr[i]


if __name__ == "__main__":
    obj = QuickSort()
    obj2 = Partitions()
    arr = [5, 13, 6, 9, 12, 8, 11]
    pivot = 5
    # obj2.naive_partition(arr, pivot)
    # print(arr)
    # print(obj2.lomuto_partition(arr, 0, len(arr) - 1))
    # print(arr)
    # arr2 = [5, 3, 8, 4, 2, 7, 1, 10]
    # print(obj2.hoarse_partition(arr2, 0, len(arr2) - 1))
    # print(arr2)

    # obj.quick_sort_loumto_partition(arr, 0, len(arr) - 1)
    # print(arr)

    obj.quick_sort_hoarse_partition(arr, 0, len(arr) - 1)
    print(arr)
