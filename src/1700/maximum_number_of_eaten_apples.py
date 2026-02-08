import heapq

class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:

        result = 0
        heap = []

        n = len(apples)

        for i in range(n):
            if apples[i]:
                heapq.heappush(heap, (i + days[i], apples[i]))
            
            while heap:
                day, n_apples = heapq.heappop(heap)
                if day <= i:
                    continue
                result += 1
                if n_apples > 1:
                    heapq.heappush(heap, (day, n_apples - 1))
                break
        i += 1
        while heap:
            day, n_apples = heapq.heappop(heap)

            if day <= i:
                continue
            
            n_eat = min(n_apples, day - i)
            result += n_eat
            i += n_eat
        return result
