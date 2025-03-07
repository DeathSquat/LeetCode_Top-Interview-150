# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: Optional[TreeNode]
        """
        self.stack = []
        self._leftmost_inorder(root)  # Initialize the stack with leftmost nodes

    def _leftmost_inorder(self, node):
        """
        Push all leftmost nodes onto the stack.
        """
        while node:
            self.stack.append(node)
            node = node.left

    def next(self):
        """
        :rtype: int
        """
        top_node = self.stack.pop()  # Get the next smallest element
        if top_node.right:
            self._leftmost_inorder(top_node.right)  # Process right subtree
        return top_node.val

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) > 0  # Check if there are elements left in stack


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
