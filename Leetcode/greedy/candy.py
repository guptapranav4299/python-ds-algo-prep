class Solution:
    def candy(self, ratings: List[int]) -> int:
        # make sure last stack is calculated
        ratings.append(float('inf'))

        # default set candy to 1
        candy = [1] * len(ratings)

        # stack init with index 0
        stack_startindex, stack_leftcandy, stack_count = 0, 1, 1

        for i in range(1, len(ratings)):

            # if rating is greater or equal : start new stack and update candy for old stack
            if ratings[i] >= ratings[i - 1]:

                # set candy to n, n-1, ......, 1 in the stack
                if stack_count > stack_leftcandy:
                    for j in range(stack_startindex, i):
                        candy[j] = stack_count
                        stack_count -= 1

                # set candy to k(leftcandy), n, n-1, ......, 1 in the stack
                else:
                    for j in range(stack_startindex + 1, i):
                        candy[j] = stack_count - 1
                        stack_count -= 1

                # set current candy to left + 1 if rating is greater
                # set current candy to 1 if rating is equal
                if ratings[i] > ratings[i - 1]:
                    candy[i] = candy[i - 1] + 1
                else:
                    candy[i] = 1

                # init new stack start from i
                stack_startindex, stack_leftcandy, stack_count = i, candy[i], 1

            # if rating is less : update stack count
            else:
                stack_count += 1

        # sum all candy except the last one we added first
        return sum(candy[:-1])