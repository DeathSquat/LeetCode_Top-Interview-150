"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        
        dummy = Node(0)  # Dummy node to track the next level's start
        prev = dummy  # Pointer to connect next level's nodes
        current = root  # Pointer to traverse current level
        
        while current:
            while current:
                # Connect left child if exists
                if current.left:
                    prev.next = current.left
                    prev = prev.next
                
                # Connect right child if exists
                if current.right:
                    prev.next = current.right
                    prev = prev.next
                
                # Move to next node at the same level
                current = current.next
            
            # Move to next level
            current = dummy.next
            dummy.next = None  # Reset dummy for the next level
            prev = dummy  # Reset prev to dummy
        
        return root
