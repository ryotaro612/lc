           
class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        found = set()
        val = 1 % k
        while val not in found and val:
            found.add(val)
            val = (val * 10 + 1) % k
        
        return -1 if val else len(found) + 1
       
