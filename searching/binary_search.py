



def linear_search(sample_list,element):
    try:
        for member in sample_list:
            if element == member:
                index_return = sample_list.index(member)
                return index_return
            else:
                pass
    except Exception as e:
        raise Exception("Error in linear search code---->",str(e))


def binary_search(sample_list,element):
    try:
        low = 0
        high = len(sample_list) - 1
        while low<=high:
            mid = (low + high) // 2
            if sample_list[mid] == element:
                return mid
            elif sample_list[mid] > element:
                low = mid - 1
            else:
                high = mid + 1

        return -1
    except Exception as e:
        raise Exception("Error in binary search---->",str(e))

def binary_search_recursive(sample_list,element,low,high):
    try:
        if low > high:
            return -1
        mid = (low + high)//2
        if sample_list[mid] == element:
            return mid
        elif sample_list[mid] > element:
            return binary_search_recursive(sample_list,element,low,mid-1)
        else:
            return binary_search_recursive(sample_list,element,mid+1,high)
    except Exception as e:
        raise Exception("Error in recursive binary search------>",str(e))



class BinarySearchProblems:

    @classmethod
    def first_occurence(cls,sample_list,element):
        try:
            low = 0
            high = len(sample_list) -1
            while low<=high:
                mid = (low+high)//2
                if sample_list[mid] == element:
                    if mid == 0 or sample_list[mid] != sample_list[mid-1]:
                        return mid
                    else:
                        high = mid - 1
                elif sample_list[mid] > element:
                    high = mid -1
                else:
                    low = mid + 1

            return -1
        except Exception as e:
            raise Exception("Error in first occurence--->",str(e))


    @classmethod
    def last_occurence(cls,sample_list,element):
        try:
            low = 0
            high = len(sample_list) -1
            while low<=high:
                mid = (low+high)//2
                if sample_list[mid] == element:
                    if mid == len(sample_list)-1 or sample_list[mid] != sample_list[mid+1]:
                        return mid
                    else:
                        low = mid + 1
                elif sample_list[mid] > element:
                    high = mid -1
                else:
                    low = mid + 1

            return -1
        except Exception as e:
            raise Exception("Error in last occurence--->",str(e))


    @classmethod
    def count_occurence(cls,sample_list,element):
        try:
            first = cls.first_occurence(sample_list,element)

            if first == -1:
                first = 0
            else:
                print("first-->", first)
                last = cls.last_occurence(sample_list,element)
                print("last--->",last)
                return last - first + 1
        except Exception as e:
            raise Exception("Error in count occurence--->",str(e))

    @classmethod
    def countOnes(cls, arr, n):
        try:
            low = 0
            high = n - 1
            while low<=high:
                mid = (low+high)//2
                if arr[mid] > 1:
                    low = mid + 1
                elif arr[mid] < 1:
                    high = mid -1
                else:
                    if mid == n-1 or arr[mid+1] != 1:
                        return mid + 1
                    else:
                        low = mid + 1
            return 0
        except Exception as e:
            raise Exception("Error in 1s count--->",str(e))

    @classmethod
    def square_root_int(cls,number):
        try:
            ans = 0
            low = 0
            high = number
            while low<=high:
                mid = (low+high)//2
                if mid**2 > number:
                    high = mid - 1
                elif mid**2 <= number:
                   ans = mid
                   low = mid + 1

            return ans
        except Exception as e:
            print("Error in square root--->",str(e))
if __name__ == '__main__':
    # sorted list
    # sample_list = [10,10,40,40,70,70,70]
    # sample_list = [20,70,70,70,70,70,70]
    # oneslist = [1,1,1,1,1,0,0,0]
    oneslist = [0,0,0]
    # sample_list = [1,1,1,1,1,0,0,0]
    element = 70
    # print(linear_search(sample_list,element))
    # print(binary_search(sample_list,element))
    # print(binary_search_recursive(sample_list,element,0,len(sample_list)-1))
    obj = BinarySearchProblems()
    # print(obj.first_occurence(sample_list,element))
    # print(obj.last_occurence(sample_list,element))
    # print(obj.count_occurence(sample_list,element))
    # print(obj.countOnes(oneslist,len(oneslist)))
    print(obj.square_root_int(element))

