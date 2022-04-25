class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        dest = 0
        for i in range(n):
            if nums[i] != val:
                nums[dest] = nums[i]
                dest += 1
        return dest
                
