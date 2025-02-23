class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        num_index = {}  # Dictionary to store the last seen index of each number
        
        for i, num in enumerate(nums):
            if num in num_index and abs(i - num_index[num]) <= k:
                return True  # Found duplicate within range k
            
            num_index[num] = i  # Update the last seen index
        
        return False
