class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return 0
        
        jumps = 0
        current_end = 0
        farthest = 0
        
        for i in range(n - 1):  # No need to check the last index
            farthest = max(farthest, i + nums[i])
            
            if i == current_end:  # Need to make a jump
                jumps += 1
                current_end = farthest
                
                if current_end >= n - 1:  # Already can reach the end
                    break
        
        return jumps
