"""
[18,64,12,21,21,78,36,58,88,58,99,26,92,91,53,10,24,25,20,92,73,63,51,65,87,6,17,32,14,42,46,65,43,9,75]
13
23

[69,10,63,24,1,71,55,46,4,61,78,21,85,52,83,77,42,21,73,2,80,99,98,89,55,94,63,50,43,62,14]
21
31
"""
import heapq


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        heap = []
        head = 0
        tail = n - 1
        for _ in range(candidates):
            heapq.heappush(heap, [costs[head], head, True])
            head += 1
        for _ in range(candidates):
            if head <= tail:
                heapq.heappush(heap, [costs[tail], tail, False])
                tail -= 1
        result = 0
        for _ in range(k):
            cost, i, is_first = heapq.heappop(heap)
            result += cost

            if head > tail:
                continue

            if is_first:
                heapq.heappush(heap, [costs[head], head, True])
                head += 1
            else:
                heapq.heappush(heap, [costs[tail], tail, False])
                tail -= 1

        return result
