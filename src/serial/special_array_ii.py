class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        """
        parity = []
        parity[i] = j # i <= j
        n = len(nums)
        parity[n-1] = n-1
        parity[i]
        nums[i] nums[i+1]
        parity[i] = parity[i+1]
        parity[i] = i

        [a, b]
        parity[a] >= b
        return
        """
        n = len(nums)
        parity = [i for i in range(n)]
        for i in range(n-2, -1, -1):
            if nums[i] % 2 != nums[i+1] % 2:
                parity[i] = parity[i+1]
            
        return [parity[start] >= end for start, end in queries ]

