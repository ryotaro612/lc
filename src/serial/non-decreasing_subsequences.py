class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result = self.rec(0, nums)
        return [lst for lst in result if len(lst) > 1]

    def rec(self, i, nums):
        if i >= len(nums):
            return []
        sub_lists = self.rec(i+1, nums)
        result = [[nums[i]]]
        for sub_list in sub_lists:
            result.append(sub_list)

            if nums[i] <= sub_list[0]:
                result.append([nums[i]] + sub_list)
        unique = dict()
        for item in result:
            unique[','.join([str(e) for e in item])] = item
        return list(unique.values())
