class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        hidden = [0]
        
        
        for e in differences:
            hidden.append(e + hidden[-1])

        mini = min(hidden)
        maxi = max(hidden)

        if lower >= mini:
            maxi += lower-mini
        else: # < 
            maxi -= mini - lower
        
        if maxi <= upper:
            return upper - maxi + 1
        
        return 0
