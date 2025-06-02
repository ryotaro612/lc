from collections import defaultdict
class Solution:
    def minimizeConcatenatedLength(self, words: List[str]) -> int:
        suffix = {(words[0][0], words[0][-1]): len(words[0])}
        n = len(words)
        for i in range(1, n):
            next_suffix = defaultdict(lambda: float('inf'))
            for p, s in suffix:
                key = (p, words[i][-1])
                n_concat = suffix[(p, s)] + len(words[i])
                if s == words[i][0]:
                    next_suffix[key] = min(next_suffix[key], n_concat - 1)
                else:
                    next_suffix[key] = min(next_suffix[key], n_concat)

                key = (words[i][0], s)
                if words[i][-1] == p:
                    next_suffix[key] = min(next_suffix[key], n_concat - 1)
                else:
                    next_suffix[key] = min(next_suffix[key], n_concat)
            suffix = next_suffix
        
        return min(suffix.values())
