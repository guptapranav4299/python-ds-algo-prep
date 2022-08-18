from collections import deque


class TPSorting:
    # time - o(v + e) space - o(v + e)
    def bfs_sorting(self, adj, v):
        indegree = [0 for i in range(v)]
        for i in range(v):
            for u in adj[i]:
                indegree[u] += 1

        q = deque()

        for i in range(v):
            if indegree[i] == 0:
                q.append(i)

        while q:
            u = q.popleft()
            print(u, end=" ")
            for x in adj[u]:
                indegree[x] -= 1
                if indegree[x] == 0:
                    q.append(x)

    def dfs(self, adj, v, stk, visited):
        visited[v] = True

        for u in adj[v]:
            if visited[u] is False:
                self.dfs(adj, u, stk, visited)

        stk.append(v)

    # time - o(v+e) space- o(v+e)
    def dfs_topological_sorting(self, adj, v):
        visited = [False] * len(adj)
        st = []

        for u in range(v):
            if visited[u] is False:
                self.dfs(adj, u, st, visited)

        while st:
            print(st.pop(), end="->")

    def add_edge(self, adj, u, v):
        adj[u].append(v)

    def print_graph(self, adj):
        ls = []
        for l in adj:
            ls.append(l)
        return ls


if __name__ == "__main__":
    obj = TPSorting()
    adj = [[2, 3], [3, 4], [3], [], []]
    v = 5
    obj.bfs_sorting(adj, v)
    print()
    v1 = 5
    # adj1 = [[] for i in range(v1)]
    # obj.add_edge(adj1, 0, 1)
    # obj.add_edge(adj1, 1, 3)
    # obj.add_edge(adj1, 2, 3)
    # obj.add_edge(adj1, 3, 4)
    # obj.add_edge(adj1, 2, 4)
    # print(adj1)
    adj1 = [[1], [3], [3, 4], [4], []]
    obj.dfs_topological_sorting(adj1, v1)
