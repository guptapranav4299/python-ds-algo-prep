import sys


class ArrayProblems:

    @classmethod
    def largestElement(cls,arr):
        try:
            result = -sys.maxsize -1
            for element in arr:
                if element > result:
                    result = element
            return result
        except Exception as e:
            raise Exception("Error in largest element---->",str(e))

    @classmethod
    def secondLargest(cls,arr):
        try:
            largest = arr[0]
            secondLargest = None
            for element in arr[1:]:
                if element > largest:
                    secondLargest = largest
                    largest = element
                elif element != largest:
                    if secondLargest is None or secondLargest < element:
                        secondLargest = element

            return secondLargest
        except Exception as e:
            raise Exception("Error in second largest----->",str(e))

    @classmethod
    def isListSorted(cls,arr):
        result = False
        try:
            for idx in range(0,len(arr)-1):
                if arr[idx] <= arr[idx+1]:
                    result = True
                else:
                    result = False
                    break

            return result
        except Exception as e:
            raise Exception("Error in sorted list---->",str(e))

    @classmethod
    def reverseList(cls,arr):
        try:
            lis = []
            for idx in range(len(arr)-1,-1,-1):
                lis.append(arr[idx])
            return lis
        except Exception as e:
            raise Exception("Error in reversing list----->",str(e))

    @classmethod
    def leftRotateByDplaces(cls,arr,d):
        try:
            pass
        except Exception as e:
            raise Exception("Error in left rotate---->",str(e))

if __name__ == '__main__':
    obj = ArrayProblems()
    arr = [10,5,20,8,9]
    # sorted_arr = [5,7,8,9,10]
    sorted_arr = [1,2,0,0]
    print(obj.largestElement(arr))
    print(obj.secondLargest(arr))
    print(obj.isListSorted(sorted_arr))
    print(obj.reverseList(arr))