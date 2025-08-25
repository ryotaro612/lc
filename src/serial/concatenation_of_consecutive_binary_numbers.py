class Solution:
    def concatenatedBinary(self, n: int) -> int:
        """
        result = 0
        mod = 10**9 + 7
        l = [0] * n
        n = 3, -> 1, 10, 11
        l[2] = 0
        l[1] = 2
        l[0] = 4

        result += i * pow(2, l[i]) % mod
        """
        # 0b<binary>
        result = 0
        shift = 1
        mod = 10**9 + 7
        for i in range(n, 0, -1):
            result += i * shift % mod
            result %= mod
            for _ in range(len(bin(i))-2):
                shift *= 2
                shift %= mod
                
        return result    
