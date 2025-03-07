import bisect

class Solution:

    def __init__(self):
        bound = 1000001
        a = [True for _ in range(bound)]
        a[0] = False
        a[1] = False
        self.primes = []
        for start in range(bound):
            if a[start]:
                for i in range(start+start, bound, start):
                    a[i] = False
                
                self.primes.append(start)
        

    def closestPrimes(self, left: int, right: int) -> List[int]:
        i = bisect.bisect_left(self.primes, left)
        if i >= len(self.primes) -1:
            return [-1, -1]
        
        diff = float('inf')
        res = [-1, -1]
        for j in range(i, len(self.primes)-1):
            if self.primes[j+1] > right:
                break
            cand = self.primes[j+1] - self.primes[j]
            if diff > cand:
                diff = cand
                res = [self.primes[j], self.primes[j+1]]
        return res
