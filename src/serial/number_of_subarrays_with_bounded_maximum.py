class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        
        lst = []
        result = 0 
        for num in nums:
            if right < num:
                result += self.sub(lst, left)
                lst = []
            else:
                lst.append(num)
        
        result += self.sub(lst, left)
        return result

    def sub(self, lst, left):
        result = len(lst) * (len(lst)+1) // 2

        sub = []
        for e in lst:
            if e < left:
                sub.append(e)
            else:
                result -= len(sub) * (1 + len(sub)) // 2
                sub = []
        if sub:
            result -= len(sub) * (1 + len(sub)) // 2
        return result
