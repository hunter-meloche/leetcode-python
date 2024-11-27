class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""
        for c in s:
            if c.isalnum():
                cleaned += c.lower()
        j = len(cleaned) - 1
        i = 0
        while i < j:
            if cleaned[i] == cleaned[j]:
                i += 1
                j -= 1
            else:
                return False
        return True
