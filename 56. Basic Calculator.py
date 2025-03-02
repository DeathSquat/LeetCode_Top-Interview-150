class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        num = 0
        sign = 1  # 1 for positive, -1 for negative
        result = 0
        
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)  # Build the number
            elif char in "+-":
                result += sign * num  # Apply the last number
                num = 0
                sign = 1 if char == "+" else -1  # Update sign
            elif char == "(":
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif char == ")":
                result += sign * num  # Apply the last number before closing
                num = 0
                result *= stack.pop()  # Multiply by the sign before '('
                result += stack.pop()  # Add result before '('
        
        return result + (sign * num)  # Add any remaining number


# Example usage:
# obj = Solution()
# print(obj.calculate("1 + 1"))  # Output: 2
# print(obj.calculate(" 2-1 + 2 "))  # Output: 3
# print(obj.calculate("(1+(4+5+2)-3)+(6+8)"))  # Output: 23
