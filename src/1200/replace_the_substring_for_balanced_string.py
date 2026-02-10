from collections import Counter
class Solution:
    def balancedString(self, s: str) -> int:
        counter = Counter(s)
        left = 0
        result = n = len(s)
        for right, c in enumerate(s):
            counter[c] -= 1
            while left < n and all(counter[c] <= n // 4 for c in 'QWER'):
                result = min(result, right - left + 1)
                counter[s[left]] += 1
                left += 1
        return result
