"""

[2, 3, 4, 5] 4
skip 0 - 1,2, <= 0-3

stairs = []
stairs[i] < stairs[i+1]
stairs[-1] >= new height
"""
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        n = len(heights)
        result = 0
        for i in range(n):
            # print('current', stack)
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                # print('reduce',stack)
                height = heights[stack.pop()]
                width = i - 1 - stack[-1]
                result = max(result, height * width)
                # print('max', result)
            stack.append(i)
        while stack[-1] != -1:
            # print('end', stack)
            height = heights[stack.pop()]
            width = n - 1 - stack[-1]
            result = max(result, height * width)
        return result
