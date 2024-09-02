class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        sum_chalk = sum(chalk)
        k %= sum_chalk
        for i in range(len(chalk)):
            if chalk[i] > k:
                return i
            k -= chalk[i]
        
        return len(chalk) - 1
