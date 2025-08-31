class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        """

        """
        result = []
        for num in nums:
            if num == 2:
                result.append(-1)
                continue
            
            bit = bin(num)[2:]
            if len(bit) == len([b for b in bit if b== '1']):
                result.append(2**(len(bit)-1) - 1)
                continue
            
            i = 0
            while num & (1<<i):
                i += 1
            
            result.append(num ^ (1<<(i-1)))
        
        return result
