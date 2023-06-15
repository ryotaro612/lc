"""
"DDIIDI" -> [3,2,1,4,6,5,7]
"""
import heapq


class Solution:
    def findPermutation(self, s: str) -> List[int]:
        stk = [1]
        perm = []
        v = 2
        for c in s:
            if c == "I":
                while stk:
                    perm.append(stk.pop())
            stk.append(v)
            v += 1
        perm.extend(stk[::-1])
        return perm
