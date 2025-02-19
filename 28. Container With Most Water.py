class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # Initialize two pointers
        left, right = 0, len(height) - 1
        max_area = 0

        # Move the pointers towards each other
        while left < right:
            # Calculate the area
            width = right - left
            area = min(height[left], height[right]) * width
            max_area = max(max_area, area)

            # Move the pointer pointing to the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
