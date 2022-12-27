

class Solution:
    def isUgly(self, n: int) -> bool:

        if n <= 0:
            return False

        while True:
            for prime in [2, 3, 5]:
                if n % prime == 0:
                    n //= prime
                    break
            else:
                break
        
        return n == 1
