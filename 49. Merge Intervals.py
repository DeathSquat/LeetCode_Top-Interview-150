class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # Sort intervals by their start times
        intervals.sort(key=lambda x: x[0])
        
        merged = []
        for interval in intervals:
            # If merged list is empty or current interval does not overlap with the previous one
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # Merge the intervals by updating the end time
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged
