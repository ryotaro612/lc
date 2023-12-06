class Solution:
    def totalMoney(self, n: int) -> int:
        result = 0
        base = 1
        while True:
            plus = base
            for _ in range(7):
                if n:
                    result += plus
                    plus += 1
                    n -= 1
                else:
                    return result
            base += 1
