class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        parts = path.split("/")

        for part in parts:
            if part == "..":
                if stack:
                    stack.pop()  # Go up one directory
            elif part and part != ".":
                stack.append(part)  # Add valid directory name

        return "/" + "/".join(stack)
