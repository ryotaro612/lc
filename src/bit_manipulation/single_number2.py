class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for i in range(33):
            n_0 = 0
            n_1 = 0
            for num in nums:
                if (1 << i) & num:
                    n_1 += 1
                else:
                    n_0 += 0
                
            if n_1 % 3:
                result |= 1 << i
        # print(bin(result))
        if result & (1 << 32):
            result &= (1 << 32) - 1
            result |= ~0 << 32
        return result
