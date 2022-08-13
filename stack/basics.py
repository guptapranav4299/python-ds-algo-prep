"""
1. Stack As List
"""


print("---------------Stack as List---------------------------------------")
st = []
print("---------Append func to push in stack---------")
st.append(10)
st.append(20)
st.append(30)
print(st)
print("---------Pop func to pop in stack---------")
print(st.pop())
print(st)
print("---------Top func to get top in stack---------")
print(st[-1])
print("---------Length of stack---------")
print(len(st))

from collections import deque


"""
2. Stack From Deque
"""
print("-------------------Stack from Deque----------------------------------")
stack = deque()
print("---------Append func to push in stack---------")
stack.append(10)
stack.append(20)
stack.append(30)
print(stack)
print("---------Pop func to pop in stack---------")
print(stack.pop())
print(stack)
print("---------Top func to get top in stack---------")
print(stack[-1])
print("---------Length of stack---------")
print(len(stack))
