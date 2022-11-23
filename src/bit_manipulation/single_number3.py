class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        x = 0
        for num in nums:
            x ^= num
            
        diff = x & -x
        
        a = 0
        for num in nums:
            if diff & num:
                a ^= num
        
        b = a
        for num in nums:
            
            b ^= num
            
        return [a, b]
