class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = [1]
        for _ in range(n-1):
            result.append(self.succ(result[-1], n))
        return result

    def succ(self, cur, n):
        if cur * 10 <= n:
            return cur * 10

        if cur % 10 < 9 and cur + 1 <= n:
            return cur + 1
        cur //= 10
        while cur % 10 == 9:
            cur //= 10
        return cur + 1
