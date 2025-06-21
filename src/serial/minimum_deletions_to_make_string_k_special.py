from collections import Counter
import math
class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        counter = Counter(word)
        freqs = sorted([f for f in counter.values()])

        result = math.inf
        n = len(freqs)
        right = 0
        total = sum(freqs)
        count = 0

        for left in range(n):
            right = max(right, left)
            while right < n and freqs[right] - freqs[left] <= k:
                count += freqs[right]
                right += 1
            
            result = min(result, total - (count + (n-right) * (freqs[left]+k)))
            count -= freqs[left]
        return result
