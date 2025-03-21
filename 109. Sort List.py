# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head  # Base case: empty list or single node
        
        # Step 1: Split the list into two halves using slow & fast pointers
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow.next
        slow.next = None  # Cut the list into two halves
        
        # Step 2: Recursively sort both halves
        left = self.sortList(head)
        right = self.sortList(mid)
        
        # Step 3: Merge the two sorted halves
        return self.merge(left, right)
    
    def merge(self, l1, l2):
        """Merge two sorted linked lists."""
        dummy = ListNode(0)
        current = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                current.next, l1 = l1, l1.next
            else:
                current.next, l2 = l2, l2.next
            current = current.next
        
        current.next = l1 or l2  # Append the remaining elements
        
        return dummy.next
