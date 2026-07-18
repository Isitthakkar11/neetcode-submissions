"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clones = {}

        def dfs(original):
            if original in clones:
                return clones[original]

            copy = Node(original.val)
            clones[original] = copy

            for nei in original.neighbors:
                copy.neighbors.append(dfs(nei))

            return copy

        return dfs(node) if node else None
        