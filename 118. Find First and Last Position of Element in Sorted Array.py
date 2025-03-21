class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def findBound(isFirst):
            left, right = 0, len(nums) - 1
            bound = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    bound = mid
                    if isFirst:
                        right = mid - 1  # Continue searching on the left
                    else:
                        left = mid + 1  # Continue searching on the right
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return bound

        # Find the first and last positions of the target
        firstPos = findBound(True)
        if firstPos == -1:  # If the target is not found, return [-1, -1]
            return [-1, -1]

        lastPos = findBound(False)
        return [firstPos, lastPos]
