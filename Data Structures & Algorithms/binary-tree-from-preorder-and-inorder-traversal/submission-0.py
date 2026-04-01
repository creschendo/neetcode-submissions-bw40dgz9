# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index = {}

        for i in range(len(inorder)):
            index[inorder[i]] = i

        self.pre_index = 0

        def helper(left, right):
            if left > right:
                return None
            
            rootValue = preorder[self.pre_index]
            self.pre_index += 1

            root = TreeNode(rootValue)

            mid = index[rootValue]

            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)

            return root
        
        return helper(0, len(index) - 1)
