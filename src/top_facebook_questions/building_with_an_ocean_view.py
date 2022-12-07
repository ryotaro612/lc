class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        result = []
        h = 0
        n = len(heights)
        for i in range(n-1, -1, -1):
            if heights[i] > h:
                result.append(i)
            h = max(h, heights[i])
            
        return result[::-1]
        
