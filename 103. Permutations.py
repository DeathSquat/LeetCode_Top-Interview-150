class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(start):
            # If we've reached the end of the array, store the permutation
            if start == len(nums):
                result.append(nums[:])  # Make a copy of nums
                return
            
            for i in range(start, len(nums)):
                # Swap the current element with the start element
                nums[start], nums[i] = nums[i], nums[start]
                # Recurse with the next index as the start
                backtrack(start + 1)
                # Backtrack (undo the swap)
                nums[start], nums[i] = nums[i], nums[start]
        
        result = []
        backtrack(0)
        return result
