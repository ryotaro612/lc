from collections import defaultdict
class Solution:
    def smallestValue(self, n: int) -> int:
        """
        2*2*3
        7
        """
        while True:
            freq = self.prime_fact(n)
            # print(freq)
            temp = 0
            for prime, f in freq.items():
                temp += prime * f

            if temp == n:
                return temp
            n = temp
    
    def prime_fact(self, n):
        freq = defaultdict(int)
        i = 2
        while i * i <= n:
            if n % i == 0:
                freq[i]+= 1
                n  = n // i
            else:
                i += 1
        if n > 1:
            freq[n] += 1
        
        return freq
