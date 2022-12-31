class Solution:
    def reverseVowels(self, s: str) -> str:
        v = set('aeiouAEIOU')
        vowels = [c for c in s if c in v]
        result = []
        for c in s:
            if c in v:
                result.append(vowels.pop())
            else:
                result.append(c)
        
        return ''.join(result)
