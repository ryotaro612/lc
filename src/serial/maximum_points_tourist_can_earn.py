import heapq
class Solution:
    def maxScore(self, n: int, k: int, stayScore: List[List[int]], travelScore: List[List[int]]) -> int:
        """
        d[day][city] 

        (0, -points, city)
        """
        d = [[0] * n for _ in range(k+1)]

        heap = [(0, 0, city) for city in range(n)]
        heapq.heapify(heap)

        while heap:
            day, point, city = heapq.heappop(heap)
            point = -point

            if d[day][city] > point or day == k:
                continue
            
            new_point = point + stayScore[day][city]
            
            if new_point > d[day+1][city]:
                d[day+1][city] = new_point
                heapq.heappush(heap, (day+1, -new_point, city))
            
            for s_city in range(n):
                new_point = point + travelScore[city][s_city]
                if d[day+1][s_city] < new_point:
                    d[day+1][s_city] = new_point
                    heapq.heappush(heap, (day+1, -new_point, s_city))
        
        return max([point for row in d for point in row])
