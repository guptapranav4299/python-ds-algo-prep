

class SubArrayProblems:
    @classmethod
    def printPairs(cls,arr):
        try:
            ls = []
            for i in range(0,len(arr)):
                for j in range(i+1,len(arr)):
                   ls.append((arr[i],arr[j]))
            return ls
        except Exception as e:
            raise Exception("Error in printing pairs-->",str(e))

    @classmethod
    def printAllSubLists(cls,arr):
        try:
            main_list = []
            for i in range(0,len(arr)):
                main_list.append(arr[i])
                for j in range(i+1,len(arr)):
                   ls = []
                   for k in range(i,j+1):
                       ls.append(arr[k])
                   main_list.append(ls)
            return main_list
        except Exception as e:
            raise Exception("Error in printing all subarrays--->",str(e))

    @classmethod
    def printAllSubListsRecursion(cls,arr,start,end):
        try:
            if end == len(arr):
                return
            if start > end:
                cls.printAllSubListsRecursion(arr,0,end+1)
            else:
                print(arr[start:end+1],end=" ")
                print()
                return cls.printAllSubListsRecursion(arr,start+1,end)
        except Exception as e:
            raise Exception("Error in printing all subarrays--->",str(e))


    # N^3
    @classmethod
    def subArraySumBruteForce(cls,arr):
        try:
            largestSum = 0
            for i in range(0,len(arr)):
                for j in range(i+1,len(arr)):
                   currentSum = 0
                   for k in range(i,j+1):
                       currentSum+= arr[k]

                   largestSum = max(currentSum,largestSum)

            return largestSum
        except Exception as e:
            raise Exception("Error in Sub Array Sum--->",str(e))


    @classmethod
    def subArraySumPrefixSum(cls,arr):
        try:
            ls = []
            largestSum = 0
            prefix_sum =arr[0]
            ls.append(arr[0])
            for i in range(1,len(arr)):
                prefix_sum+=arr[i]
                ls.append(prefix_sum)

            for i in range(0,len(arr)):
                for j in range(i+1,len(arr)):
                    currentSum = 0
                    currentSum = ls[j] - ls[i-1] if i > 0 else ls[j]
                    largestSum = max(currentSum,largestSum)
            return largestSum
        except Exception as e:
            raise Exception("Error in sub array sum prefix--->",str(e))

class QuestionClass:
    pass


if __name__ == '__main__':
    obj = QuestionClass()
    obj1 = SubArrayProblems()
    arrSum = [-2,3,4,-1,5,-12,6,1,3]
    arr = [10,20,5,15,8,9]
    print(obj1.subArraySumBruteForce(arrSum))
    print(obj1.subArraySumPrefixSum(arrSum))
    print(obj1.printPairs(arr))
    print(obj1.printAllSubLists(arr))
    obj1.printAllSubListsRecursion(arr,0,0)