# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        # Create a dummy node to simplify edge cases
        dummy = ListNode(0)
        dummy.next = head

        # Initialize two pointers
        first = dummy
        second = dummy

        # Move the first pointer n + 1 steps ahead
        for _ in range(n + 1):
            first = first.next

        # Move both pointers until the first pointer reaches the end
        while first is not None:
            first = first.next
            second = second.next

        # Remove the nth node from the end
        second.next = second.next.next

        # Return the head of the modified list
        return dummy.next
