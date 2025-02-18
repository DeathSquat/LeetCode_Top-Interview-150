class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = float('inf')  # Initialize min price to a very high value
        max_profit = 0  # Initialize max profit to 0

        for price in prices:
            if price < min_price:
                min_price = price  # Update min price if a lower price is found
            else:
                max_profit = max(max_profit, price - min_price)  # Calculate profit

        return max_profit
