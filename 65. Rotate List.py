# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head or not head.next or k == 0:
            return head
        
        # Step 1: Calculate the length of the linked list
        length = 1
        current = head
        while current.next:
            current = current.next
            length += 1
        
        # Step 2: Find the effective rotations needed
        k %= length
        if k == 0:
            return head
        
        # Step 3: Make the list circular
        current.next = head  # Connect the tail to the head to form a circle
        
        # Step 4: Find the new tail and new head
        steps_to_new_tail = length - k
        new_tail = head
        for _ in range(steps_to_new_tail - 1):
            new_tail = new_tail.next
        new_head = new_tail.next
        
        # Step 5: Break the circle
        new_tail.next = None
        
        return new_head
