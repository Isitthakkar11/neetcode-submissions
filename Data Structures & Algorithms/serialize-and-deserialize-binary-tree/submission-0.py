# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        out = []

        def dfs(node):
            if not node:
                out.append("N")
                return
            out.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(out)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        tokens = data.split(",")
        self.i = 0

        def build():
            if tokens[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(tokens[self.i]))
            self.i += 1
            node.left = build()
            node.right = build()
            return node

        return build()

