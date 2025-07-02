from collections import defaultdict
class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        right = 0
        n = len(s)
        result = 0
        for left in range(n):
            right = max(left, right)
            
            while right < n and (not freq or max(freq.values()) < k):
                freq[s[right]] += 1
                right += 1

            if max(freq.values()) >= k:
                result += n - right + 1
            
            freq[s[left]] -= 1

        return result
