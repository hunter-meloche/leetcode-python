class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # Sets in math cannot have duplicate values
        # Converting the list to a set removes duplicate values for O(n) time complexity
        # My previous O(n^2) solution used nested for loops to iterate and compare values
        # Credit to https://leetcode.com/problems/contains-duplicate/solutions/1215124/python-solutions/
        return len(set(nums)) < len(nums)
