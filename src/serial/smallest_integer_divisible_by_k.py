class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        """
        # 1 % k
        mod = 1 % k
        mod * 10 + 1 % 
        """
        found = set()
        val = 1
        while True:
            if val % k == 0:
                return len(found) + 1
            
            if val % k in found:
                return -1
            
            found.add(val % k)
            val = val % k * 10 + 1
            
