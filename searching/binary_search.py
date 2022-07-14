



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


    @classmethod
    def square_root_decimal(cls,number,p):
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

            increase = 0.1
            for i in range(0,p):
                while (ans**2 <= number):
                    ans +=increase
                    # print(ans)

                ans = ans - increase
                increase = increase/10.0
            return ans
        except Exception as e:
            print("Error in square root--->",str(e))

    @classmethod
    def rotatedSearch(cls,arr,element):
        try:
            low = 0
            high = len(arr) - 1
            while(low<=high):
                mid = (low+high)//2

                if arr[mid] == element:
                    return mid
                # left side
                if arr[low] <= arr[mid]:
                    if (element > arr[low] and element < arr[mid]):
                        high = mid - 1
                    else:
                        low = mid + 1
                else:
                    if( element > arr[mid+1] and element < arr[high]):
                        low = mid + 1
                    else:
                        high = mid - 1

            return -1
        except Exception as e:
            raise Exception("Error in rotated search----->",str(e))



    @classmethod
    def canPlaceBird(cls,arr,n,b,sep):
        try:
            birds = 1
            location = arr[0]
            for i in range(1,n):
                current_location = arr[i]
                if (current_location-location >= sep):
                    birds+=1
                    location = current_location
                    if birds == b:
                        return True

            return False
        except Exception as e:
            raise Exception("Error in can place bird---->",str(e))

    @classmethod
    def angryBirds(cls,arr,n,b):
        try:
            low = 0
            high = arr[n-1] - arr[0]
            ans = -1
            while low <= high:
                mid = (low+high)//2
                canReplace = cls.canPlaceBird(arr,n,b,mid)
                if canReplace:
                    ans = mid
                    low = mid + 1
                else:
                    high = mid - 1
            return ans
        except Exception as e:
            raise Exception("Error in angry birds------>",str(e))


# this solution is for Majority element in array [count> n/2]
class MooreVotingAlgo:
    @classmethod
    def findMajorityElement(cls,arr):
        try:
            count = 0
            idx = 0
            for i in range(len(arr)):
                if arr[idx] == arr[i]:
                    count +=1
                else:
                    count -= 1
                if count==0:
                    idx = i
                    count = 1
            return arr[idx]
        except Exception as e:
            raise Exception("Error in find majority element--->",str(e))


    @classmethod
    def checkMajority(cls,arr,element):
        try:
            count = 0
            for i in range(len(arr)):
                if arr[i] == element:
                    count+=1

            if count > (len(arr)//2):
                return True
            else:
                return False
        except Exception as e:
            raise Exception("Error in check majority element--->",str(e))

    @classmethod
    def printMajorityElement(cls,arr):
        try:
            element = cls.findMajorityElement(arr)
            if cls.checkMajority(arr,element):
                return element
            else:
                return -1

        except Exception as e:
            raise Exception("Error in printing majority element")

if __name__ == '__main__':
    # sorted list
    # sample_list = [10,10,40,40,70,70,70]
    # sample_list = [20,70,70,70,70,70,70]
    # sample_list = [4,5,6,7,1,2,3]
    # oneslist = [1,1,1,1,1,0,0,0]
    # oneslist = [0,0,0]
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
    # print(obj.square_root_int(element))
    # obj1 = MooreVotingAlgo()
    # sample_list = [1,2,3,3,4,3,3,3,3,3]
    # print(obj1.printMajorityElement(sample_list))
    # print(obj.rotatedSearch(sample_list,2))
    # print(round(obj.square_root_decimal(element,3),3))
    sample_list = [1,2,4,8,9]
    print(obj.angryBirds(sample_list,5,3))


