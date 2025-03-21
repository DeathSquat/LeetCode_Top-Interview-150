class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        
        # Initialize variables to track the lowest cost and max profit
        buy1 = buy2 = float('inf')
        profit1 = profit2 = 0
        
        for price in prices:
            # First transaction: buy at the lowest price
            buy1 = min(buy1, price)
            profit1 = max(profit1, price - buy1)
            
            # Second transaction: buy after first profit is made
            buy2 = min(buy2, price - profit1)
            profit2 = max(profit2, price - buy2)
        
        return profit2
