class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Dictionaries in Python are implemented as hash tables
        # Average lookup for hash tables is O(1), worst case O(n)
        dictionary = {}

        # Iterating through the length of the List is O(n)
        # For each iteration, a constant amount of work is done O(1)
        # Overall time complexity is O(n)
        for i, num in enumerate(nums):
            difference = target - num
            if difference not in dictionary:
                dictionary[num] = i
            else:
                return [dictionary[difference], i]
