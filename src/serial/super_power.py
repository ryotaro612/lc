class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        """
        pows[i] = a^i
        pows[0] = 1
        pows[1] = a
        pows[2] =a * a
        pows[2*i] = pows[i] * pows[i]
        """
        p = int(''.join([str(d) for d in b]))
        pows = dict()
        pows[0] = 1
        pows[1] = a
        i = 1
        mod = 1337
        while True:
            pows[i+i] = pows[i] * pows[i] % mod
            i = i + i
            if i >= p:
                break
        
        result = 1
        for i in [k for k in pows.keys()][::-1]:
            if p >= i:
                p -= i
                result = result * pows[i] % mod
        return result
                
