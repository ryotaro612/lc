import bisect

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        ub = 1
        lb = 0

 
        time = 0
        while True:
            count = 0
            time += 1
            
            mid = (ub + lb) / 2
            
            cand = []
            for i in range(len(arr)):
            
                j = bisect.bisect_left(arr, mid, 0, i, key=lambda e: e/arr[i])
                count += j
                if j:
                    cand.append([arr[j-1]/arr[i], arr[j-1], arr[i]])
            if count < k:
                lb = mid
            elif k < count:
                ub = mid
            else:
                cand.sort()
                return cand[-1][1:]

