import math


class Prims:

    # time - (v*v) space - o(v)
    def find_min_weight(self, graph, v):
        key = [math.inf] * v
        res = 0
        key[0] = 0
        mset = [False] * v
        for count in range(v):
            u = -1
            for i in range(v):
                if (mset[i] == False) and (u == -1 or key[i] < key[u]):
                    u = i
            mset[u] = True
            res += key[u]
            for j in range(v):
                if graph[u][j] != 0 and mset[j] == False:
                    key[j] = min(key[j], graph[u][j])

        return res


if __name__ == "__main__":
    pr = Prims()
    v1 = 4
    graph = [[0, 5, 8, 0], [5, 0, 10, 15], [8, 10, 0, 20], [0, 15, 20, 0]]
    print(pr.find_min_weight(graph, v1))