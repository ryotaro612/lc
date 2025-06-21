from collections import Counter
import math
class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        counter =Counter(word)
        freqs = list(counter.values())
        n = len(freqs)
        
        result = math.inf
        for i in range(n):
            deleted = 0
            for j in range(n):
                if freqs[i] < freqs[j]:
                    deleted += max(0, freqs[j] - (freqs[i] + k))
                elif freqs[j] < freqs[i]:
                    deleted += freqs[j]

            result = min(result, deleted)
        
        return result
