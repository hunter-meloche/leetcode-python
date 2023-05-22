class Solution(object):
    def __init__(self):
        self.mem = {0: 0}
    
    def coinChange(self, coins, amount):
        coins.sort() # If one of the coins is greater than amount, this breaks unless the array is sorted
        minCoins = self.getMinCoins(coins, amount)
        
        if minCoins == float('inf'):
            return -1
        
        return minCoins
            
    def getMinCoins(self, coins, amount):
        # Checks if mem already has amount's value as a key in its dictionary
        # Example: amount = 3; mem = {0:0, 1:1, 2:2, 3:1}; return 1
        if amount in self.mem:
            # Returns the value if the key is found
            return self.mem[amount]
        
        minCoins = float('inf')
        
        for c in coins:
            # If the sum of the current stack of coins is greater than amount, the loop stops adding coins
            if amount - c <  0:
                break
				
            # Attempts to find a minimum stack of coins that it can add itself to without exceeding amount
            numCoins = self.getMinCoins(coins, amount - c) + 1
            minCoins = min(numCoins, minCoins)
        
        # Adds the size of the number of coins in the current stack to the key equal to amount in the mem dictionary
        # Example: minCoins = 4; amount = 16; mem[16] = 4
        self.mem[amount] = minCoins
        
        return minCoins
        
