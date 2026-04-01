# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def count(root, seen):
            if not root:
                return 0
            
            good = 1 if root.val >= seen else 0
            return good + count(root.left, max(seen, root.val)) + count(root.right, max(seen, root.val))
        return count(root, -101)