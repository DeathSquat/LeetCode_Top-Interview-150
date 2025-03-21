import bisect

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        # O(n log n) approach using binary search and a greedy method
        sub = []
        for num in nums:
            i = bisect.bisect_left(sub, num)  # Find the insertion point
            if i == len(sub):
                sub.append(num)  # Append if num is larger than all elements
            else:
                sub[i] = num  # Replace the element at the found position
        
        return len(sub)
