# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0, head)  # Dummy node to handle edge cases
        prev = dummy  # Pointer to track last distinct node

        while head:
            # Check if the current node is a duplicate
            if head.next and head.val == head.next.val:
                # Skip all nodes with the same value
                while head.next and head.val == head.next.val:
                    head = head.next
                # Connect prev to the next distinct node
                prev.next = head.next
            else:
                prev = prev.next  # Move prev pointer if no duplicate
            
            head = head.next  # Move head pointer

        return dummy.next  # Return the updated list without duplicates
