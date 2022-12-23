import math

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # 1.. n
        # [1 .. n], prefix, nth
        # len([..]) = 1 len(prefix) == n - 1 1

        return self.rec([i for i in range(1, n+1, 1)], [], k)

    def rec(self, digits, prefix, k):
        if len(digits) == 0:
            return ''.join([str(d) for d in prefix])

        n_permutations = math.factorial(len(digits) - 1)
        n_count = 0        
        for digit in digits:
            if k <= n_count + n_permutations:
                remain = [d for d in digits if d != digit]
                return self.rec(remain, prefix + [digit], k - n_count)
            else:
                n_count += n_permutations
