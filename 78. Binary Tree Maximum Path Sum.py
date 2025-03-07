# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.max_sum = float('-inf')  # Initialize max sum to a very small number

        def dfs(node):
            if not node:
                return 0  # Base case: return 0 for null nodes
            
            # Compute the maximum path sum for left and right subtrees
            left_gain = max(dfs(node.left), 0)  # Ignore negative sums
            right_gain = max(dfs(node.right), 0)
            
            # Calculate the price of the current path that passes through the node
            current_path_sum = node.val + left_gain + right_gain
            
            # Update the global max path sum
            self.max_sum = max(self.max_sum, current_path_sum)
            
            # Return the max path sum that can be extended to the parent
            return node.val + max(left_gain, right_gain)

        dfs(root)  # Start DFS from the root
        return self.max_sum
