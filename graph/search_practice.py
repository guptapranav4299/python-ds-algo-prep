from collections import deque


class GraphSearch:
    def bfs(self, adj, vtx):
        visited = [False] * len(adj)
        q = deque()
        q.append(vtx)
        visited[vtx] = True

        while q:
            vtx = q.popleft()
            print(vtx, end="->")
            for u in adj[vtx]:
                if visited[u] is False:
                    q.append(u)
                    visited[u] = True

    def dfs(self, adj, vtx):
        visited = [False] * len(adj)
        self.dfs_util(adj, vtx, visited)

    def dfs_util(self, adj, vtx, visited):
        visited[vtx] = True
        print(vtx, end="->")
        for u in adj[vtx]:
            if visited[u] is False:
                self.dfs_util(adj, u, visited)


if __name__ == "__main__":
    adj = [[1, 2], [0, 3, 4], [0, 3], [1, 2, 4], [1, 3]]
    obj = GraphSearch()
    print("---------BFS-------------")
    obj.bfs(adj, 0)
    print()
    print("----------DFS------------")
    obj.dfs(adj, 0)