# Q69.
# Given a non-negative integer x, compute and return the square root of x.
# Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.
# Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.

# Example 1:
# Input: x = 4
# Output: 2

# Example 2:
# Input: x = 8
# Output: 2

# Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.

# Constraints:
#     0 <= x <= 231 - 1


class Solution:
    def mySqrt(self, x: int) -> int:
        try:
            low = 0
            high = x
            result = None
            while low <= high:
                mid = (low + high) // 2
                if mid * mid > x:
                    high = mid - 1
                elif mid * mid <= x:
                    result = mid
                    low = mid + 1
                else:
                    pass
            return result
        except Exception as e:
            raise Exception("Error in mySqrt---->",str(e))

    def mySqrt_2pointer(self, x: int) -> int:
        try:
            if (x < 1):
                return 0
            end = x
            start = 1
            while (start < end):
                mid = start + (end - start) // 2
                print("Mid--->",mid)
                print("start-->",start)
                print("end--->",end)
                print("x//mid--->",x//mid)
                print("x-->",x)
                if (mid == x // mid or start == mid):
                    return mid
                elif (mid > x // mid):
                    end=mid
                else:
                    start=mid
                print("--------->")
            return start
        except Exception as e:
            raise Exception("Error in mySqrt---->",str(e))

if __name__ == "__main__":
    obj = Solution()
    x = 10
    print(obj.mySqrt(x))
    print(obj.mySqrt_2pointer(x))
