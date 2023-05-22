class Solution:
    def climbStairs(self, n: int) -> int:
        a = 1
        b = 0
        # Finds the n+1th Fibonacci number
        for i in range(1, n+1):
            c = a + b
            b = a
            a = c
        return a 
