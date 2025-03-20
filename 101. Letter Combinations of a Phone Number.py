class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # Mapping of digits to corresponding letters
        digit_to_char = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

        # If the input is empty, return an empty list
        if not digits:
            return []

        # Recursive function to generate combinations
        def backtrack(index, current_combination):
            # If the current combination has a length equal to the input digits, add it to results
            if index == len(digits):
                combinations.append("".join(current_combination))
                return

            # Get the possible letters for the current digit
            possible_letters = digit_to_char[digits[index]]
            
            # Iterate through these letters and recurse
            for letter in possible_letters:
                current_combination.append(letter)  # Choose
                backtrack(index + 1, current_combination)  # Explore
                current_combination.pop()  # Un-choose

        combinations = []
        backtrack(0, [])
        return combinations
