class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        """
        1, 2
        1, 3
        1, 4
        2, 3

        """
        v_points = [1] + sorted(vFences) + [n]
        h_points = [1] + sorted(hFences) + [m]

        lengths = set()
        for i in range(len(v_points)):
            for j in range(i+1, len(v_points)):
                lengths.add(v_points[j] - v_points[i])
        
        result = -1
        for i in range(len(h_points)):
            for j in range(i+1, len(h_points)):
                edge = (h_points[j] - h_points[i])
                if edge in lengths:
                    result = max(result, edge**2)
        if result < 0:
            return result
        return result % (10**9+7)
