class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] > nums[mid + 1]:
                # If mid is greater than next element, peak must be on the left side or at mid
                right = mid
            else:
                # If mid is smaller than next element, peak must be on the right side
                left = mid + 1
        
        return left  # or return right, both will be at peak index
