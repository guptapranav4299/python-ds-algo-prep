from collections import deque


class Solution:
    # time - o(v + e) space - o(v + e)
    def cycle_detection_dfs(self, adj, s):
        visited = [False] * len(adj)
        recstk = [False] * len(adj)
        for i in range(s):
            if visited[i] is False:
                if self.cycle_detection_dfs_util(adj, i, visited, recstk):
                    return True
        return False

    def cycle_detection_dfs_util(self, adj, s, visited, recstk):
        visited[s] = True
        recstk[s] = True
        for u in adj[s]:
            if visited[u] is False and self.cycle_detection_dfs_util(adj, u, visited, recstk):
                return True
            elif recstk[u]:
                return True

        recstk[s] = False
        return False

    def kahns_algo(self, adj , v):
        indegree = [0 for i in range(v)]
        for i in range(v):
            for u in adj[i]:
                indegree[u] += 1

        q = deque()

        for i in range(v):
            if indegree[i] == 0:
                q.append(i)

        count = 0
        while q:
            u = q.popleft()
            for x in adj[u]:
                indegree[x] -= 1
                if indegree[x] == 0:
                    q.append(x)
            count += 1

        if count != v:
            return True
        else:
            return False


if __name__ == "__main__":
    obj = Solution()
    adj = [[1], [0, 2], [1, 3], [2, 4, 5], [3, 5], [4, 3]]
    v = 6
    print(obj.cycle_detection_dfs(adj, v))

    adj1 = [[1], [2], [3], [1], [1]]
    v1 = 5
    print(obj.kahns_algo(adj1, v1))