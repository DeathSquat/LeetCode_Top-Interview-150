from collections import defaultdict
from fractions import Fraction

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points) <= 1:
            return len(points)
        
        max_count = 1
        
        for i in range(len(points)):
            slopes = defaultdict(int)
            duplicate = 0
            local_max = 0
            
            for j in range(i + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                
                if x1 == x2 and y1 == y2:
                    duplicate += 1
                    continue
                
                slope = Fraction(y2 - y1, x2 - x1) if x1 != x2 else "inf"
                slopes[slope] += 1
                local_max = max(local_max, slopes[slope])
            
            max_count = max(max_count, local_max + duplicate + 1)
        
        return max_count
