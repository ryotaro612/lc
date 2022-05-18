class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        
        sub_permutes = self.permuteUnique(nums[1:])
        items = []
        
        for sub_permute in sub_permutes:
            n = len(sub_permute)
            for i in range(n):
                items.append(sub_permute[:i] + [nums[0]] + sub_permute[i:])
            items.append(sub_permute + [nums[0]])
        items = sorted(items)
        result = [items[0]]
        for item in items[1:]:
            if result[-1] != item:
                result.append(item)
        return result
