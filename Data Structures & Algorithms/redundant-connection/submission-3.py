class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n + 1))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for a, b in edges:
            root_a = find(a)
            root_b = find(b)
            if root_a == root_b:
                return [a, b]
            parent[root_b] = root_a

        return[]
 