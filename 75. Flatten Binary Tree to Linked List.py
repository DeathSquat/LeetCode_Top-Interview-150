# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        
        # Flatten the left and right subtrees
        self.flatten(root.left)
        self.flatten(root.right)
        
        # Store the right subtree
        temp_right = root.right
        
        # Move the left subtree to the right
        root.right = root.left
        root.left = None  # Ensure left is null
        
        # Move to the rightmost node of the new right subtree
        current = root
        while current.right:
            current = current.right
        
        # Attach the stored right subtree
        current.right = temp_right
