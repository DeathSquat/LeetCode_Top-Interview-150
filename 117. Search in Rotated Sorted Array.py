class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            # Check if the target is at mid
            if nums[mid] == target:
                return mid
            
            # Determine which part of the array is sorted
            if nums[left] <= nums[mid]:
                # Left half is sorted
                if nums[left] <= target < nums[mid]:
                    right = mid - 1  # Target is in the sorted left half
                else:
                    left = mid + 1  # Target is in the right half
            else:
                # Right half is sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1  # Target is in the sorted right half
                else:
                    right = mid - 1  # Target is in the left half
        
        return -1  # Target is not found
