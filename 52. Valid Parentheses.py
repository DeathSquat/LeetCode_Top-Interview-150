class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping:
                # Pop the top element from the stack if it's not empty, else assign a dummy value
                top_element = stack.pop() if stack else '#'
                # Check if the popped element matches the current closing bracket
                if mapping[char] != top_element:
                    return False
            else:
                # It's an opening bracket, push it onto the stack
                stack.append(char)

        # If the stack is empty, all brackets were matched
        return not stack
