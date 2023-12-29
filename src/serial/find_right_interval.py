import bisect

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        """
        Time Complexity: O(n log n)
        Space Complexity: O(n)
        """
        order = sorted([[v[0], i] for i, v in enumerate(intervals)])
        n = len(order)
        result = []
        for _, end in intervals:
            i = bisect.bisect_left(order, end, key=lambda e: e[0])
            if i < n:
                result.append(order[i][1])
            else:
                result.append(-1)
        return result
       
