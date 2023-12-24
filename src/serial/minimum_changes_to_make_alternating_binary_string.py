class Solution:
    def minOperations(self, s: str) -> int:
        # 010101
        count = 0
        # 101010
        count2 = 0
        for i, c in enumerate(s):
            if i % 2:
                if c == '0':
                    count += 1
                else:
                    count2 += 1
            else:
                if c == '1':
                    count += 1
                else:
                    count2 += 1
        return min(count, count2)
