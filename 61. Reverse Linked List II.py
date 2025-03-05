# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        if not head or left == right:
            return head  # No need to reverse if there's only one node or left == right
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # Move `prev` to the node before `left`
        for _ in range(left - 1):
            prev = prev.next

        # Reverse the sublist from `left` to `right`
        current = prev.next
        next_node = None

        for _ in range(right - left):
            temp = current.next
            current.next = temp.next
            temp.next = prev.next
            prev.next = temp
        
        return dummy.next
