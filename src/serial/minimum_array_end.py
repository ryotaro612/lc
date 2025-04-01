class Solution:
    def minEnd(self, n: int, x: int) -> int:
        """
        x = 10101
             * *
             2^2
             nums[n-1]
             argmin x, n <= x^2
        """
        result = 0
        j = 0

        for i in range(64):    
            if x & (1<<i):
                result |= (1 << i)
            else:
                if (n-1)  & (1<< j):
                    result |= (1<<i)
                j += 1
        return result
        

    
