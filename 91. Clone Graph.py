"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None
        
        # Dictionary to store cloned nodes
        clones = {}

        def dfs(curr_node):
            if curr_node in clones:
                return clones[curr_node]  # Return already cloned node
            
            # Clone the current node
            clone = Node(curr_node.val)
            clones[curr_node] = clone  # Store it in the map
            
            # Clone all the neighbors recursively
            for neighbor in curr_node.neighbors:
                clone.neighbors.append(dfs(neighbor))
            
            return clone

        return dfs(node)
