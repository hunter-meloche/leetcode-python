class Solution:
    def climbStairs(self, n: int) -> int:
        a = 1
        b = 0
        # Finds the n+1th Fibonacci number
        for i in range(n):
            a = a + b
            b = a - b
        return a 
