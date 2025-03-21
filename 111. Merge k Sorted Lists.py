# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        import heapq

        class Wrapper:
            def __init__(self, node):
                self.node = node

            def __lt__(self, other):
                return self.node.val < other.node.val

        min_heap = []

        # Add the head of each linked list to the heap
        for linked_list in lists:
            if linked_list:
                heapq.heappush(min_heap, Wrapper(linked_list))

        dummy = ListNode(0)
        current = dummy

        # Extract the smallest element and add the next node from the same list
        while min_heap:
            smallest = heapq.heappop(min_heap).node
            current.next = smallest
            current = current.next
            if smallest.next:
                heapq.heappush(min_heap, Wrapper(smallest.next))

        return dummy.next
