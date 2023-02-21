from collections import Counter

class Solution:
    def minimumKeypresses(self, s: str) -> int:
        counter = Counter(s)

        order = sorted([c for c in counter], key=lambda c: counter[c], reverse=True)
        c_to_i = {c: i for i, c in enumerate(order)}
        result = 0
        for c, freq in counter.items():
            if c_to_i[c] < 9:
                result += freq
            elif c_to_i[c] < 18:
                result += freq * 2
            else:
                result += freq * 3
        return result 
