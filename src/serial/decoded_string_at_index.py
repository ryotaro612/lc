class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        count = 0
        for c in s:
            if c.isdigit():
                if k <= count * int(c):
                    if k % count:
                        return self.decodeAtIndex(s, k % count)
                    else:
                        return self.decodeAtIndex(s, count)
                else:
                    count *= int(c)
            else:
                count += 1
                if count == k:
                    return c
