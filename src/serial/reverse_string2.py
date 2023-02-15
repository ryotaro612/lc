class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        lst = [c for c in s]
        result = []
        for i in range(0, len(s), 2*k):
            fragment = lst[i:i+2*k]
            result.extend(fragment[:k][::-1])
            result.extend(fragment[k:])
        return ''.join(result)
