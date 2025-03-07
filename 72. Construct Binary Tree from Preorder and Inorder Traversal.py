# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        if not preorder or not inorder:
            return None
        
        # The first element of preorder is the root of the tree
        root_val = preorder.pop(0)
        root = TreeNode(root_val)

        # Find the index of the root in inorder
        inorder_index = inorder.index(root_val)

        # Recursively build left and right subtrees
        root.left = self.buildTree(preorder, inorder[:inorder_index])
        root.right = self.buildTree(preorder, inorder[inorder_index + 1:])

        return root
