class Solution:
    def pivotInteger(self, n: int) -> int:
        """
        sum [1, n] -> n * (n+1) / 2
        sum [i, j] -> j * (j+1) // 2 - (i-1)*i//2
        n + )
        """
        lb, ub = 0, n+1
        while ub - lb > 1:
            mid = (lb + ub) // 2
            left = self.seq_sum(1, mid)
            right = self.seq_sum(mid, n)
            if left < right:
                lb = mid
            elif left > right:
                ub = mid
            else:
                return mid
        return -1 
        
    def seq_sum(self, left, right):
        """
        [left, right]
        """
        return right * (right+1) // 2 - (left-1) * left // 2
