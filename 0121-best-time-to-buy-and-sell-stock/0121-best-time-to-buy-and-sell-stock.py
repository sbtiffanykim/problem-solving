class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = sys.maxsize

        for price in prices:
            min_price = min(price, min_price)  # Track the lowest price so far
            max_profit = max(price - min_price, max_profit)  # Update max profit if selling today yields more profit
    
        return max_profit
