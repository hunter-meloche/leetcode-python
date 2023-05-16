class Solution:
    def getSum(self, a: int, b: int) -> int:
        # python integers are can be infinite in size
        # mask allows for us to treat them as 32-bit integers
        mask = 0xffffffff

        # the loop will continue while there is still a remainder after each xor
        while b:
            sum = (a^b) & mask # binary xor addition filtered through mask
            carry = ((a&b)<<1) & mask # gets the remainder and applies mask
            a = sum # replaced by the sum of both numbers
            b = carry # b now holds the remainder
            
        # checks if the sum is a negative number by checking if there is a 1 in the 32nd bit
        if (a>>31) & 1:
            return (a&mask) - 0x100000000 # returns negative sum by subtracting the maximum 32-bit integer plus 1
        return a # returns positive sum
