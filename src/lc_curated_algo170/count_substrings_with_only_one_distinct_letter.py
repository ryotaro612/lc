class Solution:
    def countLetters(self, s: str) -> int:
        n = len(s)
        res = 0
        left = 0
        for right in range(n):
            if s[left] == s[right]:
                continue
            else:
                # print(left, right)
                res += (right - left) * (right - left + 1) // 2
                left = right
        right += 1
        res += (right -left) * (right -left + 1) // 2
        return res
