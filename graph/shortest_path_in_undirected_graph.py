import math
from collections import deque


class Solution:

    # time - o(v + e) space - o(v + e)
    def shortest_path(self, adj, vtx):
        distance =[math.inf] * len(adj)
        distance[vtx] = 0
        q = deque()
        q.append(vtx)
        visited = [False] * len(adj)
        visited[vtx] = True

        while q:
            s = q.popleft()
            for u in adj[s]:
                if visited[u] is False:
                    distance[u] = distance[s] + 1
                    visited[u] = True
                    q.append(u)

        return distance


if __name__ == "__main__":
    obj = Solution()
    adj = [[1, 2], [0, 2, 3], [1, 3, 0], [2, 1]]
    print(obj.shortest_path(adj, 0))
