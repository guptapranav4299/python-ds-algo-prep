class SortingQuestions:
    @classmethod
    def merge_2_sorted_lists_naive(cls,arr1,arr2):
        try:
            a = []
            a = arr1 + arr2
            a = sorted(a)
            return a
        except Exception as e:
            raise Exception("Error in merging 2 sorted list naive------>",str(e))


    @classmethod
    def merge_2_sorted_lists(cls,arr1,arr2):
        try:
            i = 0
            j = 0
            n = len(arr1)
            m = len(arr2)
            result = []
            while i < n and j < m:
                if arr1[i] < arr2[j]:
                    result.append(arr1[i])
                    i += 1
                else:
                    result.append(arr2[j])
                    j += 1

            while i < n:
                result.append(arr1[i])
                i += 1

            while j < m:
                result.append(arr2[j])
                j += 1

            return result
        except Exception as e:
            raise Exception("Error in merging 2 sorted list------>",str(e))



class MergeSortQuestions:
    @classmethod
    def count_inversion(cls,arr,l,r):
        res = 0
        if l < r:
            mid = (l + r) //2
            res +=cls.count_inversion(arr,l,mid)
            res += cls.count_inversion(arr,mid+1,r)
            res+=cls.merge_inversions(arr,l,mid,r)
        return res

    @classmethod
    def merge_inversions(cls,arr,low,mid,high):
        left = arr[low:mid+1]
        right = arr[mid+1:high+1]
        res,i,j,k = 0,0,0,low

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i+=1
                k+=1
            else:
                arr[k] = right[j]
                j+=1
                k+=1
                res+= (len(left) - i)

        while i < len(left):
            arr[k] = left[i]
            i+=1
            k+=1

        while j < len(right):
            arr[k] = right[j]
            j+=1
            k+=1

        return res



if __name__ == "__main__":
    obj = SortingQuestions()
    # a = [10,15]
    # b = [5,6,6,30,40]
    # print(obj.merge_2_sorted_lists_naive(a,b))
    # print(obj.merge_2_sorted_lists(a,b))

    merge_obj = MergeSortQuestions()
    arr = [2,4,1,3,5]
    print(merge_obj.count_inversion(arr,0,len(arr)-1))
