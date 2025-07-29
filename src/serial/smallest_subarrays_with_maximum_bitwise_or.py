class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        """
        result = []
        bit_index = []
        bit_index[i]
        bx10010
            i
        bit_index[0] contains 0
        
        nums[j]
        result[j] = k - j + 1
        """
        bound = 32
        bit_index = [[] for _ in range(bound)]
        for i, num in enumerate(nums):
            j = 0
            while num:
                if num & 1:
                    bit_index[j].append(i)
                num >>= 1
                j += 1
        
        for i in range(bound):
            bit_index[i] = bit_index[i][::-1]
        
        result = []
        for i, num in enumerate(nums):
            cand = []
            for j in range(bound):
                while bit_index[j] and bit_index[j][-1] < i:
                    bit_index[j].pop()

                if bit_index[j]:
                    cand.append(bit_index[j][-1])
            
            if cand:
                result.append(max(cand) - i + 1)
            else:
                result.append(1)
        return result
