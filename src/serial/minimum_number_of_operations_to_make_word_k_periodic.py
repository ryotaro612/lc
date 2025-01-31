from collections import defaultdict
class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        freq = defaultdict(int)

        mx_freq = 0
        for i in range(0, len(word), k):
            freq[word[i:i+k]] += 1
            mx_freq = max(mx_freq, freq[word[i:i+k]])
        
        return len(word) // k - mx_freq
