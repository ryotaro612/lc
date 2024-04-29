class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        xor = 0
        for num in nums:
            xor = xor ^ num
        
        result = 0
        pos = 0
        while (xor >> pos) != (k >> pos):
            if (xor >> pos) % 2 != (k >> pos) % 2:
                result += 1
            pos += 1
        
        return result
