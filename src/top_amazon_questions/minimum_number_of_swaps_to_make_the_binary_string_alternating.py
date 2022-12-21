from collections import Counter
class Solution:
    def minSwaps(self, s: str) -> int:
        n = len(s)
        # 010101...
        if n % 2 == 0:
            freq = {'0': n // 2, '1': n // 2}
        else:
            freq = {'0': n // 2 + 1, '1': n // 2}

        counter = Counter(s)
        result = float('inf')
        if freq['0'] == counter['0'] or freq['1'] == counter['1']:
            n_diff = 0
            for i, c in enumerate(s):
                if i % 2:
                    if c == '0':
                        n_diff += 1
                else:
                    if c == '1':
                        n_diff += 1
            result = n_diff
        # 1010101..
        freq['0'], freq['1'] = freq['1'], freq['0']
        if freq['0'] == counter['0'] or freq['1'] == counter['1']:
            n_diff = 0
            for i, c in enumerate(s):
                if i % 2:
                    if c == '1':
                        n_diff += 1
                else:
                    if c == '0':
                        n_diff += 1
            result = min(result, n_diff)
        
        if result == float('inf'):
            return -1
        else:
            return result // 2
        
