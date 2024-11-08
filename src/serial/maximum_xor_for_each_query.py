class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        x = 0
        for num in nums:
            x ^= num
        result = []
        while nums:
            e = 0
            for i in range(maximumBit):
                if (x & (1<<i)) == 0:
                    e |= 1 << i
            result.append(e)
            x ^= nums.pop()
    
        return result
