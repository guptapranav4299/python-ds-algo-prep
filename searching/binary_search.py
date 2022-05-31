



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


if __name__ == '__main__':
    sample_list = [10,20,30,40,50,60,70]
    element = 40
    print(linear_search(sample_list,element))
    print(binary_search(sample_list,element))
    print(binary_search_recursive(sample_list,element,0,len(sample_list)-1))