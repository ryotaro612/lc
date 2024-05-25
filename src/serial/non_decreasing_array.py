class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        return self.rec(0, nums, True)

    def rec(self, i, nums, available):
        n = len(nums)
        # print(nums)
        if i == n - 1:
            return True

        if nums[i] > nums[i+1]:
            if available:
                if i:
                    temp = nums[i]
                    nums[i] = nums[i-1]
                    if self.rec(i, nums, False):
                        return True
                    nums[i] = temp
                    nums[i+1] = nums[i]
                    return self.rec(i, nums, False)
                else:
                    nums[i] = -float('inf')
                    return self.rec(i, nums, False)
            else:
                return False

        return self.rec(i+1, nums, available)
