class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        end = 0
        freq = dict()
        
        result = 0
        for start in range(len(s)):
            while end < len(s):
                c = s[end]
                if c in freq:
                    freq[c] += 1
                    end += 1
                    result = max(result, end - start)
                    continue
                else:
                    if len(freq) < k:
                        freq[c] = 1
                        end += 1
                        result = max(result, end-start)
                    else:
                        break
            freq[s[start]] -= 1
            if freq[s[start]] == 0:
                del freq[s[start]]
        return result
