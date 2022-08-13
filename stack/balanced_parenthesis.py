class Solution:
    def isValid(self, s: str) -> bool:
        def is_matching(ele, x):
            if (ele == '(' and x == ')') or (ele == '{' and x == '}') or (ele == '[' and x == ']'):
                return True
            else:
                return False

        st = []
        for x in s:
            if x in ('(', '{', '['):
                st.append(x)
            else:
                if not st:
                    return False
                elif not is_matching(st[-1], x):
                    return False
                else:
                    st.pop()
        if st:
            return False
        else:
            return True


if __name__ == "__main__":
    obj = Solution()
    s = "()[]{}"
    print(obj.isValid(s))
