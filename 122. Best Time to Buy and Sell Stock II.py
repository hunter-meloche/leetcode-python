class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # Tracking the lowest possible buy price as the list is iterated through bypasses the need for nested loops
        # It is initially given the first value of the list and the value will be updated upon finding a lower value in the list
        min_buy = prices[0]
        max_profit = 0

        # The iterator starts at 1 AKA the second position in the list
        # The list is iterated through only once, so overall time complexity is O(n)
        for i in range(1, len(prices)):

            # min_buy always precedes prices[i] in the list, so it is always a valid comparison
            profit = prices[i] - min_buy

            if max_profit < profit:
                max_profit = profit

            # Any comparison after this assignment takes place after the value's position in the list
            if min_buy > prices[i]:
                min_buy = prices[i]
        
        return max_profit
