import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        done = set()

        result = []
        heap = []
        heapq.heappush(heap, (nums1[0] + nums2[0], 0, 0))
        done.add((0, 0))
        n1, n2 = len(nums1), len(nums2)

        while len(result) < k and heap:
            _, i, j = heapq.heappop(heap)
            result.append([nums1[i], nums2[j]])

            if i < n1 - 1 and (i+1, j) not in done:
                done.add((i+1, j))
                heapq.heappush(heap, (nums1[i+1]+nums2[j], i+1, j))
            if j < n2 - 1 and (i, j+1) not in done:
                done.add((i, j+1))
                heapq.heappush(heap, (nums1[i] + nums2[j+1], i, j+1))
        return result
