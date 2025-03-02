class MinStack(object):

    def __init__(self):
        """
        Initialize two stacks:
        - `stack`: Stores all values.
        - `min_stack`: Stores the minimum value at each level.
        """
        self.stack = []
        self.min_stack = []

    def push(self, val):
        """
        Push val onto the stack and update min_stack.
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        # Push the new minimum value to min_stack
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        """
        Remove the top element from the stack and update min_stack.
        :rtype: None
        """
        if self.stack:
            if self.stack[-1] == self.min_stack[-1]:
                self.min_stack.pop()
            self.stack.pop()

    def top(self):
        """
        Get the top element of the stack.
        :rtype: int
        """
        return self.stack[-1] if self.stack else None

    def getMin(self):
        """
        Retrieve the minimum element in the stack.
        :rtype: int
        """
        return self.min_stack[-1] if self.min_stack else None


# Example usage:
# obj = MinStack()
# obj.push(-2)
# obj.push(0)
# obj.push(-3)
# print(obj.getMin())  # Output: -3
# obj.pop()
# print(obj.top())    # Output: 0
# print(obj.getMin()) # Output: -2
