class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = [w for w in s.split(' ') if len(w) > 0]
        return len(words[-1])
