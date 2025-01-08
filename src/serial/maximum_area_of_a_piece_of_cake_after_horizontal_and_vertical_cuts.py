class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        if horizontalCuts[0] != 0:
            horizontalCuts  = [0] + horizontalCuts
        if horizontalCuts[-1] != h:
            horizontalCuts.append(h)
        
        verticalCuts.sort()
        if verticalCuts[0] != 0:
            verticalCuts = [0] + verticalCuts
        if verticalCuts[-1] != w:
            verticalCuts.append(w)
        height = 0
        for i in range(len(horizontalCuts)-1):
            height = max(height, horizontalCuts[i+1] - horizontalCuts[i])
        width = 0
        for i in range(len(verticalCuts) -1 ):
            width = max(width, verticalCuts[i+1] - verticalCuts[i])
        
        return height * width % (10**9 + 7)
