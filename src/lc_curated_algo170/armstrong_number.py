class Solution:
    def isArmstrong(self, n: int) -> bool:
        s = str(n)
        l = len(s)
        return sum([(ord(c) - ord('0')) ** l for c in s]) == n
