class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []
        
        def backtrack(start, path):
            if len(path) == k:
                result.append(path[:])  # Make a copy of path
                return
            
            for i in range(start, n + 1):
                path.append(i)  # Choose
                backtrack(i + 1, path)  # Explore
                path.pop()  # Un-choose
        
        backtrack(1, [])
        return result
