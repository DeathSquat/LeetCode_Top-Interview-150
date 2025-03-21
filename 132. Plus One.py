class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        
        # Traverse the digits array from -the last element
        for i in range(n - 1, -1, -1):
            # If the current digit is less than 9, increment it and return the result
            if digits[i] < 9:
                digits[i] += 1
                return digits
            
            # If the digit is 9, set it to 0 and continue
            digits[i] = 0
        
        # If all digits were 9, we need to add a leading 1
        return [1] + digits
