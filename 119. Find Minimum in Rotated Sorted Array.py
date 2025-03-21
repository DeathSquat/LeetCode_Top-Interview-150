class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # If mid element is greater than rightmost, min must be on right half
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                # Otherwise, min must be on left half (including mid)
                right = mid

        return nums[left]  # or nums[right], both point to the minimum element
