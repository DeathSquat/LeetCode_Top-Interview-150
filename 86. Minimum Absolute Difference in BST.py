# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.prev = None
        self.min_diff = float('inf')

        def inorder(node):
            if not node:
                return
            
            # Traverse left subtree
            inorder(node.left)

            # Compute min difference with the previous node
            if self.prev is not None:
                self.min_diff = min(self.min_diff, node.val - self.prev)
            self.prev = node.val  # Update previous node value
            
            # Traverse right subtree
            inorder(node.right)
        
        inorder(root)
        return self.min_diff
