from collections import deque, defaultdict

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # Step 1: Build the graph (Adjacency List) and in-degree array
        graph = defaultdict(list)
        in_degree = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1  # Increase in-degree of dependent course

        # Step 2: Add all courses with in-degree 0 to the queue (no prerequisites)
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        count = 0  # Number of courses we can complete

        # Step 3: Process courses in topological order
        while queue:
            course = queue.popleft()
            count += 1  # This course can be completed
            
            for next_course in graph[course]:
                in_degree[next_course] -= 1  # Reduce in-degree
                if in_degree[next_course] == 0:
                    queue.append(next_course)

        # Step 4: Check if we completed all courses
        return count == numCourses
