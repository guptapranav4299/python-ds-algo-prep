class Solution:
    def detect_cycle_dfs(self, adj , vtx):
        visited = [False] * len(adj)
        for i in range(vtx):
            if visited[i] is False:
                if self.detect_cycle_dfs_util(adj, i, visited, -1):
                    return True
        return False

    def detect_cycle_dfs_util(self, adj, v, visited, parent):
        visited[v] = True
        for u in adj[v]:
            if visited[u] is False:
                if self.detect_cycle_dfs_util(adj, u, visited, v):
                    return True
                elif u != parent:
                    return True
        return False


if __name__ == "__main__":
    obj = Solution()
    adj = [[1], [0, 2, 3], [1, 4, 3], [1, 2], [2, 5], [4]]
    print(obj.detect_cycle_dfs(adj, 6))