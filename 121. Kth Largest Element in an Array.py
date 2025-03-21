import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Min-heap of size k
        min_heap = []
        
        for num in nums:
            heapq.heappush(min_heap, num)  # Push element to heap
            if len(min_heap) > k:
                heapq.heappop(min_heap)  # Remove the smallest element
        
        return heapq.heappop(min_heap)  # The root is the kth largest element

# Example Usage:
# solution = Solution()
# print(solution.findKthLargest([3,2,1,5,6,4], 2))  # Output: 5
# print(solution.findKthLargest([3,2,3,1,2,4,5,5,6], 4))  # Output: 4
