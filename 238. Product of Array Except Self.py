class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # Credit to https://leetcode.com/problems/product-of-array-except-self/solutions/1597994/c-python-4-simple-solutions-w-explanation-prefix-suffix-product-o-1-space-approach/

        # Passed array length is used for sizing returned array and loop iteration
        length = len(nums)
        # The products arra that will be returned is initialized to be the with all 1s and the same length as nums
        prods = [1] * length
        # prefixProd accumulates the products of nums iteratively from the left
        prefixProd = 1
        # suffixProd does the same from the right side
        suffixProd = 1

        # prefixProd and suffixProd are iteratively accumulated and applied to the array of 1s starting from left-to-right and right-to-left respectively
        for i in range(length):
            prods[i] *= prefixProd
            prefixProd *= nums[i]
            prods[-1-i] *= suffixProd
            suffixProd *= nums[-1-i]
    
        return prods
