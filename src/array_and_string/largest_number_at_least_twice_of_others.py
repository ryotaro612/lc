class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        largest, pos = -1, -1
        for i, num in enumerate(nums):
            if largest < num:
                largest = num
                pos = i
                
        for i, num in enumerate(nums):
            if i == pos:
                continue
            else:
                if largest < num * 2:
                    return -1
        return pos
