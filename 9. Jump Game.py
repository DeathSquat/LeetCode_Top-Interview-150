class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_reachable = 0
        for i in range(len(nums)):
            # If the current index is not reachable, return False
            if i > max_reachable:
                return False
            # Update the maximum reachable index
            max_reachable = max(max_reachable, i + nums[i])
        return True
