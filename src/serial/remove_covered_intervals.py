class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        """
        [[4, 5],  [1, 6]]
        [[1, 1], [1, 1]]
        [[3, 6], [5, 6]]
        [[1, 7], [4, 7]]
        """

        intervals.sort(key=lambda x: (x[0], -x[1]))

        right = -1
        result = 0
        for _, b in intervals:
            if b <= right:
                result += 1
            right = max(right, b)
        
        return len(intervals) - result
