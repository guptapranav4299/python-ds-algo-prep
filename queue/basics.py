"""
Queue Implementation
"""

print("---------------Queue as List---------------------------------------")
q = []
print("---------Append func to enqueue in a queue---------")
q.append(10)
q.append(20)
q.append(30)
print(q)
print("---------Deque func to deque in queue---------")
print(q.pop(0))
print(q)
print("---------Front func to get front in queue---------")
print(q[0])
print("---------Rear func to get rear in queue---------")
print(q[-1])
print("---------Length of queue---------")
print(len(q))

from collections import deque


"""
2. Stack From Deque
"""
print("-------------------Queue from Deque----------------------------------")
queue = deque()
print("---------Append func to enqueue in queue---------")
queue.append(10)
queue.append(20)
queue.append(30)
print(queue)
print("---------Pop func to pop front from queue---------")
print(queue.popleft())
print(queue)
print("---------Front func to get front in queue---------")
print(queue[0])
print("---------Rear func to get rear in queue---------")
print(queue[-1])
print("---------Length of Queue---------")
print(len(queue))
