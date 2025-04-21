class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        prev = 0
        mini = prev
        maxi = prev
        for e in differences:
            new_e = prev + e
            maxi = max(maxi, new_e)
            mini = min(mini, new_e)
            prev = new_e
        
        maxi += lower - mini

        return max(0, upper - maxi + 1)
