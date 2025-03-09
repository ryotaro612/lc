class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        colors.extend(colors[:k-1])
        n = len(colors)
        left = right = 0
        result = 0
        while left < n:
            right = max(left, right)
            while right < n - 1 and colors[right] != colors[right+1]:
                right += 1
                if right - left + 1 >= k:
                    result += 1
            left = right = right + 1

        return result
