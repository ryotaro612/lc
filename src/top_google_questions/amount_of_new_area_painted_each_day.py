class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        max_index = max((i for item in paint for i in item))
        area = [-1] * (max_index + 1)
        result = [0] * len(paint)
        
        for i, (start, end) in enumerate(paint):
            cur = start
            while cur < end:
                if area[cur] == -1:
                    result[i] += 1
                    area[cur] = end
                    cur += 1
                else:
                    next_cur = area[cur]
                    area[cur] = max(area[cur], end)
                    cur = next_cur
        return result
