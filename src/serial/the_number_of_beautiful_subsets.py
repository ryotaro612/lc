class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        nums.sort()

        return self.rec(nums, k, 0, []) - 1

    def rec(self, nums, k, i, temp):
        if i == len(nums):
            # print(temp)
            return 1
        result = 0
        
        result += self.rec(nums, k, i+1, temp)
        if nums[i] - k not in temp:
            temp.append(nums[i])
            result += self.rec(nums, k, i+1, temp)
            temp.pop()
        # print(result, nums, i)
        return result 
