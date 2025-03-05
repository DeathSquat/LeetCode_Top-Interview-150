# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        # Helper function to reverse a linked list segment
        def reverseLinkedList(start, end):
            prev, curr = None, start
            while curr != end:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev

        dummy = ListNode(0)
        dummy.next = head
        prev_group_end = dummy

        while True:
            # Check if there are at least k nodes to reverse
            kth_node = prev_group_end
            for _ in range(k):
                kth_node = kth_node.next
                if not kth_node:
                    return dummy.next

            # Reverse k nodes
            group_start = prev_group_end.next
            next_group_start = kth_node.next

            # Break the link to reverse the group
            kth_node.next = None
            reversed_head = reverseLinkedList(group_start, None)

            # Connect the reversed group to the previous and next parts of the list
            prev_group_end.next = reversed_head
            group_start.next = next_group_start

            # Move prev_group_end to the end of the reversed group
            prev_group_end = group_start
