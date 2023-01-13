class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        freq = 0
        i = 0
        n = len(nums)
        for j in range(n):
            if j == 0:
                i = 1
                freq = 1
            elif nums[j] == nums[j-1]:
                if freq < 2:
                    nums[i] = nums[j]
                    i += 1
                    freq += 1
                else:
                    continue
            else:
                freq = 1
                nums[i] = nums[j]
                i += 1
        # print(i)
        return i
