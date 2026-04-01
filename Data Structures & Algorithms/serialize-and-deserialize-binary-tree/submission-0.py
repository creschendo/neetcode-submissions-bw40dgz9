# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        sol = []

        def helper(node):
            if not node:
                sol.append("N")
                return
            sol.append(str(node.val))
            helper(node.left)
            helper(node.right)
        helper(root)

        return ",".join(sol)
    
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        self.pos = 0

        def helper():
            if vals[self.pos] == "N":
                self.pos += 1
                return None
            root = TreeNode(int(vals[self.pos]))
            self.pos += 1
            root.left = helper()
            root.right = helper()
            return root
        return helper()