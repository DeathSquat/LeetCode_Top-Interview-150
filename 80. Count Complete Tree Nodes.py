# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        
        left_depth = self.getDepth(root.left)
        right_depth = self.getDepth(root.right)

        if left_depth == right_depth:
            # Left subtree is a full binary tree, count its nodes and recurse on right
            return (1 << left_depth) + self.countNodes(root.right)
        else:
            # Right subtree is a full binary tree, count its nodes and recurse on left
            return (1 << right_depth) + self.countNodes(root.left)

    def getDepth(self, node):
        """Returns the depth of the leftmost path in the tree."""
        depth = 0
        while node:
            depth += 1
            node = node.left
        return depth
