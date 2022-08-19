class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        result = 0
        for a, b in zip(heights, expected):
            if a != b:
                result += 1
                
        return result
