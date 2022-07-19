
class Recursion:
    def tower_of_hanoi(self, n, A, C, B):
        if n == 0:
            return
        self.tower_of_hanoi(n-1, A, B, C)
        print("Move disk", n, "from rod", A, "to rod", C)
        self.tower_of_hanoi(n-1, B, C, A)

    def josesphus_problem(self, n, k):
        if n == 1:
            return 1
        return (self.josesphus_problem(n-1 , k) + k-1) % n+1

    def power_of_two(self, n):
        if n == 0:
            return False
        elif n == 1:
            return True
        elif n % 2 == 1:
            return False
        return self.power_of_two(n//2)


    def power_of_three(self, n):
        if n == 0:
            return False
        elif n == 1:
            return True
        elif n % 3 in (1, 2):
            return False
        return self.power_of_three(n//3)

    def isArraySorted(self,idx,arr,n):
        if idx == n-1:
            return True
        if (arr[idx] < arr[idx+1] and self.isArraySorted(idx+1,arr,n)):
            return True
        else:
            return False

    def first_occurence(self,arr,idx,element,n):
        if idx == n:
            return -1
        if arr[idx] == element:
            return idx
        else:
            return self.first_occurence(arr,idx+1,element,n)


    def last_occurence(self,arr,idx,element,n):
        if idx < 0:
            return -1
        if arr[idx] == element:
            return idx
        else:
            return self.last_occurence(arr,idx-1,element,n)

    def all_occurence(self,arr,idx,element,n,result):
        if idx == n:
            return result
        if arr[idx] == element:
            result.append(idx)
            return self.all_occurence(arr,idx+1,element,n,result)
        else:
            return self.all_occurence(arr,idx+1,element,n,result)

    def power_of_n(self, x, n):
        if n == 0:
            return 1
        sub_prob = self.power_of_n(x,n//2)
        sub_prob_square = pow(sub_prob,2)
        if (n % 2 != 0):
            return x * sub_prob_square
        else:
            return sub_prob_square

    def tiling_problem(self, n, m):
        if m > n:
            return 1
        a = self.tiling_problem(n-1, m)
        b = self.tiling_problem(n-m, m)
        return a + b

    def no_of_binary_strings(self,n):
        if n == 0:
            return 1
        if n == 1:
            return 2
        return self.no_of_binary_strings(n - 1) + self.no_of_binary_strings(n - 2)

    def friend_party(self,n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.friend_party(n - 1) + (n -1)*(self.friend_party(n - 2))



if __name__ == "__main__":
    obj = Recursion()
    # n = 2
    # obj.tower_of_hanoi(n, 'A', 'C', 'B')

    # n = 5
    # k = 2
    # print(obj.josesphus_problem(n, k))

    # n = 32
    # print(obj.power_of_two(n))

    # n = 81
    # print(obj.power_of_three(n))

    # arr = [1,2,3,4,5,6]
    # arr2 = [9,8,21,3,0,1]
    # n = 6
    # print(obj.isArraySorted(0,arr,n))
    # print(obj.isArraySorted(0,arr2,n))

    # arr2 = [9,8,21,3,0,1]
    # n = 6
    # print(obj.first_occurence(arr2,0,2,n))

    # arr = [1,2,3,3,5,6,6]
    # n = 7
    # print(obj.last_occurence(arr,n-1,6,n))
    # print(obj.all_occurence(arr,0,6,n,[]))

    # x = 2
    # n = 10
    # print(obj.power_of_n(x, n))

    # n = 4
    # m = 3
    # print(obj.tiling_problem(n,m))

    # n = 3
    # print(obj.no_of_binary_strings(n))

    n = 3
    print(obj.friend_party(n))




