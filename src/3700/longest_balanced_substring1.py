from collections import defaultdict
class Solution:
    def longestBalanced(self, s: str) -> int:
        result = 0
        n = len(s)
        for left in range(n):
            freq_letters = defaultdict(set)
            letter_freq = defaultdict(int)
            for right in range(left, n):
                if s[right] in letter_freq:
                    f = letter_freq[s[right]]
                    letter_freq[s[right]] += 1
                    freq_letters[f].remove(s[right])
                    freq_letters[f + 1].add(s[right])
                    if len(freq_letters[f]) == 0:
                        del freq_letters[f]
                else:
                    letter_freq[s[right]] = 1
                    freq_letters[1].add(s[right])
            
                if len(freq_letters) == 1:
                    result = max(result, right - left + 1)

        return result 
