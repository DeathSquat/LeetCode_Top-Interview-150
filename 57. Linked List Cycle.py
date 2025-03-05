# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow, fast = head, head  # Initialize two pointers

        while fast and fast.next:
            slow = slow.next  # Moves one step
            fast = fast.next.next  # Moves two steps

            if slow == fast:  # If they meet, cycle exists
                return True

        return False  # If we exit loop, no cycle
