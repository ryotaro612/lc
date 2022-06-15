"""
Example 1
envelopes = [[2, 3], [5, 4], [6, 4], [6, 7]]
dp        = [1     ,      1,      1,      1]


[[2,100],[3,200],[4,300],[5,500],[5,400],[5,250],[6,370],[6,360],[7,380]]
"""
import bisect as bi
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda env: (env[0], -env[1]))
        lis = []
        n = len(envelopes)
        hs = [a[1] for a in envelopes]
        for i in range(n):
            idx = bi.bisect_left(lis, hs[i])
            if len(lis) == idx:
                lis.append(hs[i])
            else:
                lis[idx] = hs[i]
        return len(lis)
        
        
        
