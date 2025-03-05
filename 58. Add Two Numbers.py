# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Initialize a dummy node to form the resulting linked list
        dummy = ListNode()
        current = dummy  # Pointer to construct the new linked list
        carry = 0  # Variable to store the carry during addition

        while l1 or l2 or carry:
            # Get the values from the current nodes, or 0 if the node is None
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Compute the sum and carry
            total = val1 + val2 + carry
            carry = total // 10  # Update the carry
            current.next = ListNode(total % 10)  # Create a new node for the result
            current = current.next  # Move to the next node

            # Advance l1 and l2 to their next nodes, if they exist
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next  # Return the head of the resultant linked list
