import heapq

class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        """
        :type k: int
        :type w: int
        :type profits: List[int]
        :type capital: List[int]
        :rtype: int
        """
        # Step 1: Store (capital, profit) as tuples and sort by capital
        projects = sorted(zip(capital, profits))
        
        max_heap = []  # Max heap to store profits of affordable projects
        i = 0
        n = len(profits)

        # Step 2: Perform k iterations to maximize capital
        for _ in range(k):
            # Add all projects we can afford to max heap
            while i < n and projects[i][0] <= w:
                heapq.heappush(max_heap, -projects[i][1])  # Use negative profit to simulate max heap
                i += 1

            # If no projects are available, break early
            if not max_heap:
                break

            # Select the most profitable project
            w += -heapq.heappop(max_heap)  # Convert back from negative profit

        return w

# Example Usage:
# solution = Solution()
# print(solution.findMaximizedCapital(2, 0, [1,2,3], [0,1,1]))  # Output: 4
# print(solution.findMaximizedCapital(3, 0, [1,2,3], [0,1,2]))  # Output: 6
