import heapq

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        max_n_unique = len(set(s))
        n = len(s)
        result = 0
        for n_unique in range(1, max_n_unique+1):
            end = 0
            freq = dict()
            for start in range(n):
                end = max(end, start)

                while end < n and len(freq) <= n_unique:
                    c = s[end]
                    if c in freq:
                        freq[c] += 1
                    elif len(freq) < n_unique:
                        freq[c] = 1
                    else:
                        break
                    ok = True
                    for letter in freq:
                        if freq[letter] < k:
                            ok = False
                    if ok:
                        result = max(result, end - start + 1)
                    end += 1
                # print(n_unique, start, end, freq)
                head = s[start]
                freq[head] -= 1
                if freq[head] == 0:
                    # print('del', freq)
                    del freq[head]
        return result
