class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        return self.is_break(s1, s2) or self.is_break(s2, s1)

    def is_break(self, s1, s2):
        s1 = sorted(s1)
        s2 = sorted(s2)
        n = len(s1)
        for i in range(n):
            if s1[i] > s2[i]:
                return False
        return True
