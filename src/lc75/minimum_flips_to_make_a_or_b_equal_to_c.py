class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        result = 0
        while a or b or c: 
            ab, bb, cb = [v & 1 for v in [a, b, c]]
            if cb:
                if (ab | bb) == 0:
                    result += 1
            else:
                result += len([x for x in [ab, bb] if x])
            a, b, c = [v >> 1 for v in [a, b, c]]
        return result
