class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0

        # Sort balloons by their ending points
        points.sort(key=lambda x: x[1])

        arrows = 1  # At least one arrow is needed
        prev_end = points[0][1]  # First balloon's end point

        for start, end in points[1:]:
            # If the current balloon starts after the last shot position, we need a new arrow
            if start > prev_end:
                arrows += 1
                prev_end = end  # Update the position of the last shot

        return arrows
