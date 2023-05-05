from collections import defaultdict

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        result = 0
        counter = defaultdict(int)
        vowels = {'a', 'e', 'i', 'o', 'u'}
        for i in range(k):
            if s[i] in vowels:
                counter[s[i]] += 1
            
        
        result = max(result, sum(counter.values()))
        
        for i in range(k, len(s)):
            if s[i-k] in vowels:
                counter[s[i-k]] -= 1
            if s[i] in vowels:
                counter[s[i]] += 1
            result = max(result, sum(counter.values()))
        return result
