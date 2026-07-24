class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        edges = []
        for i in range(n):
            xi, yi = points[i]
            for j in range(i + 1, n):
                xj, yj = points[j]
                dist = abs(xi - xj) + abs(yi - yj)
                edges.append((dist, i , j))
        edges.sort()

        parent = list(range(n))
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        total, used = 0, 0
        for cost, i, j in edges:
            root_i, root_j = find(i), find(j)
            if root_i != root_j:
                parent[root_j] = root_i
                total += cost
                used += 1
                if used == n - 1:
                    break
        return total 