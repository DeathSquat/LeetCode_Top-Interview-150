from collections import deque, defaultdict

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # Step 1: Create adjacency list and in-degree array
        adj_list = defaultdict(list)
        in_degree = [0] * numCourses

        for course, prereq in prerequisites:
            adj_list[prereq].append(course)
            in_degree[course] += 1

        # Step 2: Initialize queue with courses having in-degree 0
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        course_order = []

        # Step 3: Process courses in topological order
        while queue:
            course = queue.popleft()
            course_order.append(course)

            for neighbor in adj_list[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # Step 4: Check if all courses are processed
        return course_order if len(course_order) == numCourses else []
