class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        result = 0
        letters = [0] * 26
        n = len(s)
        for i in range(n):
            if i >= k:
                letters[ord(s[i - k]) - ord("a")] -= 1

            letters[ord(s[i]) - ord("a")] += 1

            if i >= k - 1 and max(letters) <= 1:
                result += 1

        return result
