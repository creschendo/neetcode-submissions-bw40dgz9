# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def bfs(root, val) -> int:
            if not root:
                return 0
            
            left = bfs(root.left, max(val, root.val))
            right = bfs(root.right, max(val, root.val))
            return (root.val >= val) + left + right
        
        return bfs(root, float("-inf"))