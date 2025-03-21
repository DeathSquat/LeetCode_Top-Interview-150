class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_sum = sum(nums)
        
        def kadane(arr):
            max_sum = cur_sum = arr[0]
            for num in arr[1:]:
                cur_sum = max(num, cur_sum + num)
                max_sum = max(max_sum, cur_sum)
            return max_sum
        
        max_kadane = kadane(nums)  # Maximum subarray sum without wrapping

        # Compute min subarray sum
        min_kadane = kadane([-num for num in nums])  # Min subarray sum
        circular_max = total_sum + min_kadane  # Maximum sum when wrapping
        
        if circular_max == 0:
            return max_kadane  # Handles all-negative case
        
        return max(max_kadane, circular_max)
