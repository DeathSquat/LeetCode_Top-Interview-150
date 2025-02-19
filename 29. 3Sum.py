class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Sort the array to facilitate two-pointer technique
        nums.sort()
        result = []
        
        # Iterate through the array to fix the first element of the triplet
        for i in range(len(nums)):
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Initialize two pointers for the remaining part of the array
            left, right = i + 1, len(nums) - 1
            
            # Find triplets using the two-pointer technique
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum == 0:
                    # Found a triplet
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicates for the second and third elements
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # Move pointers inward
                    left += 1
                    right -= 1
                elif current_sum < 0:
                    # Increase the sum by moving the left pointer to the right
                    left += 1
                else:
                    # Decrease the sum by moving the right pointer to the left
                    right -= 1
        
        return result
