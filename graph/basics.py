from collections import deque


class UndirectedGraph:
    def add_edge(self, adj, u, v):
        adj[u].append(v)
        adj[v].append(u)

    def print_graph(self, adj):
        ls = []
        for l in adj:
            ls.append(l)
        return ls

    # time - o(v + e) space - o(v + e)
    def bfs(self, adj, vtx):
        visited = [False] * len(adj)
        q = deque()
        q.append(vtx)
        visited[vtx] = True
        while q:
            vtx = q.popleft()
            print(vtx, end=" ")
            for u in adj[vtx]:
                if visited[u] is False:
                    q.append(u)
                    visited[u] = True

    def bfs_disconnected_graph(self, adj):
        visited = [False] * len(adj)
        for u in range(len(adj)):
            if visited[u] is False:
                self.bfs_disconnected_graph_util(adj, u, visited)

    def bfs_disconnected_graph_util(self, adj, vtx, visited):
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

    # time - 0(v+e) space- o(v+e)
    def dfs(self, adj, vtx):
        visited = [False] * len(adj)
        self.dfs_util(adj, vtx, visited)

    def dfs_util(self, adj, vtx, visited):
        visited[vtx] = True
        print(vtx, end=" ")
        for u in adj[vtx]:
            if visited[u] is False:
                self.dfs_util(adj, u, visited)

    def dfs_disconnected(self, adj, vtx):
        visited = [False] * len(adj)
        for u in range(len(adj)):
            if visited[u] is False:
                self.dfs_util(adj, u, visited)


if __name__ == "__main__":
    ug = UndirectedGraph()
    v = 4
    adj = [[] for i in range(v)]
    # ug.add_edge(adj, 0, 1)
    # ug.add_edge(adj, 0, 2)
    # ug.add_edge(adj, 1, 2)
    # ug.add_edge(adj, 1, 3)
    # print("------Print this Graph-------------")
    # print(ug.print_graph(adj))
    # print("-------Print BFS of Graph-------------")
    # ug.bfs(adj,0)
    # print("--------------New Graph---------")
    # adj1 = [[1, 2], [0, 3], [0, 3], [1, 2], [5, 6], [4, 6], [4, 5]]
    # print(ug.print_graph(adj1))
    # ug.bfs_disconnected_graph(adj1)
    # print("-----------DFS Traversal of new graph--------------")
    # adj2 = [[1, 2], [0, 3, 4], [0, 3], [1, 2, 4], [1, 3]]
    # ug.dfs(adj2, 0)
    print("-----------DFS Traversal of disconnected graph--------------")
    adj3 = [[1, 2], [0, 2], [0, 1], [4], [3]]
    ug.dfs_disconnected(adj3, 0)

