import heapq

class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        n = len(arr)
        heap = []
        heapq.heappush(heap, arr[n-1])
        for i in range(n-2, -1, -1):
            if arr[i] > heap[0]:
                cand = max([v for v in heap if arr[i] > v])
                for j in range(i+1, n):
                    if arr[j] == cand:
                        arr[i], arr[j] = arr[j], arr[i]
                        return arr
            heapq.heappush(heap, arr[i])
        return arr
