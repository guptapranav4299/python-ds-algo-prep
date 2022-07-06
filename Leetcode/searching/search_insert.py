#Q.35 [Leetcode Problems]
# Given a sorted array of distinct integers and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.

# Input: nums = [1,3,5,6], target = 5
# Output: 2

# Input: nums = [1,3,5,6], target = 2
# Output: 1

# Input: nums = [1,3,5,6], target = 4
# Output: 2

# Input: nums = [1,3,5,6], target = 7
# Output: 4

def search_insert(nums,target):
    try:
        found_flag = False
        low = 0
        high = len(nums) - 1
        result_idx = None
        while low <= high:
            mid_idx = (low+high)//2
            result_idx = mid_idx
            if target < nums[mid_idx]:
                high = mid_idx - 1
            elif target > nums[mid_idx]:
                low = mid_idx + 1
            else:
                found_flag = True
                break

        if found_flag:
            return result_idx
        else:
            if nums[result_idx] < target:
                return result_idx + 1
            else:
                return result_idx

    except Exception as e:
        raise Exception("Error in Search Insert---->",str(e))


if __name__ == "__main__":
    arr1 = [1,3,5,6]
    target1 = 5
    target2 = -1
    print(search_insert(arr1,target1))
    print("--------------------------")
    print(search_insert(arr1,target2))

