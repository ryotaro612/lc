class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        vowels = set('aeiouAEIOU')
        first = 0
        second = 0
        for i in range(n//2):
            if s[i] in vowels:
                first += 1
            if s[n//2 + i] in vowels:
                second += 1
        return first == second
