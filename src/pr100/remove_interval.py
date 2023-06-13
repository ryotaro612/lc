class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        result = []

        r_a, r_b = toBeRemoved
        
        for a, b in intervals:
            if r_b <= a or b <= r_a:
                result.append([a, b])
            else:
            #  i  ----
            #  t    -----
                if a < r_a:
                    result.append([a, r_a])
            # i ------
            # t  ----
                if r_b < b:
                    result.append([r_b, b])
        return result
