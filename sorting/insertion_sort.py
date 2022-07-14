class InsertionSort:
    @classmethod
    def insertion_sort(cls,arr):
        try:
            n = len(arr)
            for i in range(1, len(arr)):
                x = arr[i]
                j = i - 1
                while j >= 0 and x < arr[j]:
                    arr[j + 1] = arr[j]
                    j = j - 1
                arr[j + 1] = x
            return arr
        except Exception as e:
            raise Exception("Error in insertion sort---------->",str(e))


    @classmethod
    def reverse_insertion_sort(cls,arr):
        try:
            n = len(arr)
            for i in range(1, len(arr)):
                x = arr[i]
                j = i - 1
                while j >= 0 and x > arr[j]:
                    arr[j + 1] = arr[j]
                    j = j - 1
                arr[j + 1] = x
            return arr
        except Exception as e:
            raise Exception("Error in  reverse insertion sort---------->",str(e))


if __name__ == '__main__':
    obj = InsertionSort()
    a = [8, 6, 9, 2, 3, 1, 0]
    print(obj.insertion_sort(a))
    print(obj.reverse_insertion_sort(a))
