"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None

        # Step 1: Clone nodes and interweave them
        cur = head
        while cur:
            new_node = Node(cur.val, cur.next, None)
            cur.next = new_node
            cur = new_node.next

        # Step 2: Assign random pointers to cloned nodes
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        # Step 3: Separate the cloned list from the original list
        cur = head
        new_head = head.next
        new_cur = new_head
        while cur:
            cur.next = cur.next.next
            if new_cur.next:
                new_cur.next = new_cur.next.next
            cur = cur.next
            new_cur = new_cur.next

        return new_head
