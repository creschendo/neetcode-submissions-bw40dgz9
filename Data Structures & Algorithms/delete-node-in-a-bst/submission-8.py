# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]: 
        def getSuccessor(node):
            node = node.right
            while node and node.left:
                node = node.left
            return node
        
        def helper(root, key):
            if not root:
                return None
            
            if root.val > key:
                root.left = helper(root.left, key)
            elif root.val < key:
               root.right = helper(root.right, key)
            else:

                if not root.left:
                    return root.right
                if not root.right:
                    return root.left
                succ = getSuccessor(root)
                root.val = succ.val
                root.right = helper(root.right, succ.val)
        
            return root
        return helper(root, key)

            