class Solution:
    def sumZero(self, n: int) -> List[int]:
        a = 1
        result = []
        for i in range(n - 1 if n % 2 else n):
            result.append(a)
            a = -a
            if a > 0:
                a += 1

        
        if n % 2:
            result.append(0)

        return result
