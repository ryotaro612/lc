class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        equiv = []
        greater = []
        for num in nums:
            if num < pivot:
                less.append(num)
            elif num == pivot:
                equiv.append(num)
            else:
                greater.append(num)
        
        return less + equiv + greater
