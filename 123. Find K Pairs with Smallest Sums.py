import heapq

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if not nums1 or not nums2:
            return []

        min_heap = []
        result = []

        # Step 1: Push the first k pairs (nums1[i], nums2[0]) into the heap
        for i in range(min(k, len(nums1))):
            heapq.heappush(min_heap, (nums1[i] + nums2[0], i, 0))  # (sum, index in nums1, index in nums2)

        # Step 2: Extract k smallest pairs
        while k > 0 and min_heap:
            sum_, i, j = heapq.heappop(min_heap)
            result.append([nums1[i], nums2[j]])

            # Move to the next element in nums2 for the same nums1[i]
            if j + 1 < len(nums2):
                heapq.heappush(min_heap, (nums1[i] + nums2[j + 1], i, j + 1))

            k -= 1

        return result

# Example Usage:
# solution = Solution()
# print(solution.kSmallestPairs([1,7,11], [2,4,6], 3))  # Output: [[1,2],[1,4],[1,6]]
# print(solution.kSmallestPairs([1,1,2], [1,2,3], 2))  # Output: [[1,1],[1,1]]
