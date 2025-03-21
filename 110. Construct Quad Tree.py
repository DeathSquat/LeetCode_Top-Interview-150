"""
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution(object):
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        def build(x, y, size):
            # Check if the current grid is uniform (all 0s or all 1s)
            value = grid[x][y]
            for i in range(x, x + size):
                for j in range(y, y + size):
                    if grid[i][j] != value:
                        # If not uniform, divide into four quadrants
                        half = size // 2
                        return Node(
                            val=True,  # Value doesn't matter for non-leaf nodes
                            isLeaf=False,
                            topLeft=build(x, y, half),
                            topRight=build(x, y + half, half),
                            bottomLeft=build(x + half, y, half),
                            bottomRight=build(x + half, y + half, half),
                        )
            # If all values are the same, create a leaf node
            return Node(val=value == 1, isLeaf=True)
        
        return build(0, 0, len(grid))
