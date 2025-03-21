class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        result = 0
        for i in range(32):
            result = (result << 1) | (n & 1)  # Shift left and add the rightmost bit of n
            n >>= 1  # Shift n right by 1
        return result
