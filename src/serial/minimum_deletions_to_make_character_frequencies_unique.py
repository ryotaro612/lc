from collections import Counter, defaultdict
class Solution:
    def minDeletions(self, s: str) -> int:
        deletions = 0
        counter = Counter(s)
        freqs = set()
        for letter, freq in counter.items():
            while freq > 0 and freq in freqs:
                deletions += 1
                freq -= 1
            freqs.add(freq)
        return deletions
