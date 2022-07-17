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



if __name__ == "__main__":
    obj = SortingQuestions()
    a = [10,15]
    b = [5,6,6,30,40]
    print(obj.merge_2_sorted_lists_naive(a,b))
    print(obj.merge_2_sorted_lists(a,b))