class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Define the Roman numeral to integer mappings
        roman_to_int = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }

        total = 0  # Initialize total to store the final result
        prev_value = 0  # Keep track of the previous numeral's value

        # Iterate through the Roman numeral string in reverse order
        for char in reversed(s):
            current_value = roman_to_int[char]  # Get the integer value of the current character

            # Check if we need to subtract or add the current value
            if current_value < prev_value:
                total -= current_value  # Subtract if current value is less than the previous value
            else:
                total += current_value  # Add otherwise

            # Update the previous value for the next iteration
            prev_value = current_value

        return total
