class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # Initialize pointers for both strings
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        result = []

        # Loop through both strings from the end
        while i >= 0 or j >= 0 or carry:
            # Get the current digit from each string or 0 if index is out of bounds
            digit_a = int(a[i]) if i >= 0 else 0
            digit_b = int(b[j]) if j >= 0 else 0

            # Compute the sum of digits and the carry
            total = digit_a + digit_b + carry
            carry = total // 2  # Carry for the next step
            result.append(total % 2)  # Add the current binary digit to the result

            # Move pointers to the left
            i -= 1
            j -= 1

        # Reverse the result list and convert to a string
        return ''.join(map(str, result[::-1]))
