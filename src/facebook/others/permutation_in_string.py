class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        char_count = dict()
        for c in s1:
            char_count[c] = 1 + char_count.get(c, 0)
        window = dict()
        right = 0
        for left in range(len(s2)):
            right = max(right, left)
            while right < len(s2):
                c  = s2[right]
                if c in char_count and char_count[c] > 0:
                    char_count[c] -= 1
                    right += 1
                    if right - left == len(s1):
                        return True
                else:
                    break
            if s2[left] in char_count:
                char_count[s2[left]] += 1
        return False
