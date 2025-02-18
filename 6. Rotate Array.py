class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n  # In case k > n

        # Reverse the entire array
        self.reverse(nums, 0, n - 1)
        # Reverse the first k elements
        self.reverse(nums, 0, k - 1)
        # Reverse the remaining elements
        self.reverse(nums, k, n - 1)

    def reverse(self, nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
