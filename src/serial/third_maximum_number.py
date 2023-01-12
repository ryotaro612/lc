class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        top_n = [max(nums)]
        for _ in range(2):
            mx = -float('inf')
            for num in nums:
                if top_n[-1] > num:
                    mx = max(mx, num)
            if mx != -float('inf'):
                top_n.append(mx)
        if len(top_n) == 3:
            return top_n[-1]
        else:
            return top_n[0]
