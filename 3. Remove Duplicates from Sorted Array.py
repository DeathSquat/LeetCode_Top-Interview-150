class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        # Initialize a pointer for the position of unique elements
        unique_pos = 0
        
        for i in range(1, len(nums)):
            if nums[i] != nums[unique_pos]:
                unique_pos += 1
                nums[unique_pos] = nums[i]
        
        return unique_pos + 1
