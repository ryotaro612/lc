from collections import Counter
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        result = 0
        counter = Counter(words)
        middle = False
        for word, freq in counter.items():
            if word[0] == word[1]:
                result += freq // 2 * 2 * 2
                if freq % 2:
                    middle = True
                continue
            
            if word[::-1] in counter:
                result += min(freq, counter[word[::-1]]) * 2
        
        return result + 2 if middle else result
