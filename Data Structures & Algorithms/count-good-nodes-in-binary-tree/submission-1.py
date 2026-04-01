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
            # recurse on left and right children, setting value to max 
            # val will always be the max seen in that path
            left = bfs(root.left, max(val, root.val))
            right = bfs(root.right, max(val, root.val))

            # return whether the current node is a good node 
            # and any good nodes in the left and right subtrees
            return (root.val >= val) + left + right
        
        return bfs(root, float("-inf"))