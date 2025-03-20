class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def backtrack(start, target, path, res):
            # Base case: if the target becomes 0, we found a combination
            if target == 0:
                res.append(list(path))
                return
            
            # Iterate through the candidates
            for i in range(start, len(candidates)):
                # If the candidate exceeds the target, skip it
                if candidates[i] > target:
                    continue
                
                # Include the candidate and backtrack
                path.append(candidates[i])
                backtrack(i, target - candidates[i], path, res)
                path.pop()  # Undo the choice

        result = []
        backtrack(0, target, [], result)
        return result
