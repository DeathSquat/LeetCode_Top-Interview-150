import heapq

class MedianFinder:

    def __init__(self):
        # Max-heap for the left half (store negative values to simulate max-heap)
        self.left = []
        # Min-heap for the right half
        self.right = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        # Add to max-heap (left)
        heapq.heappush(self.left, -num)

        # Balance by moving the largest from left to right
        heapq.heappush(self.right, -heapq.heappop(self.left))

        # Ensure left heap has at least as many elements as right heap
        if len(self.left) < len(self.right):
            heapq.heappush(self.left, -heapq.heappop(self.right))

    def findMedian(self):
        """
        :rtype: float
        """
        # If odd number of elements, return the max of left heap
        if len(self.left) > len(self.right):
            return -self.left[0]
        # If even, return the average of max from left and min from right
        return (-self.left[0] + self.right[0]) / 2.0

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
