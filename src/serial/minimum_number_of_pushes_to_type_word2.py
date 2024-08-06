from collections import Counter, defaultdict
class Solution:
    def minimumPushes(self, word: str) -> int:
        counter = Counter(word)
        order = sorted([[counter[c], c] for c in counter], reverse=True)
        mapping = [[] for _ in range(8)]
        i = 0
        for _, c in order:
            mapping[i].append(c)
            i += 1
            i %= 8
        c_to_time = dict()
        for element in mapping:
            for i, c in enumerate(element):
                c_to_time[c] = i + 1
        
        
        return sum([c_to_time[c] for c in word])
