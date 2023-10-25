import heapq

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        found = set()
        heap = [1] + primes
        heapq.heapify(heap)

        while True:
            v = heapq.heappop(heap)
            if v not in found:
                found.add(v)
                if len(found) == n:
                    return v
                for prime in primes:
                    heapq.heappush(heap, v * prime)
        
