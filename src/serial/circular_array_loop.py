"""
[-2,-3,-9]
"""
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        return self.find_loop(nums) or self.find_loop([-v for v in nums][::-1])
    def find_loop(self, nums):
        n = len(nums)
        visit = [False] * n
        for i in range(n):
            if visit[i]:
                continue
            passed = set()
            cur = i
            while True:
                visit[cur] = True
                if nums[cur] < 0 or cur == (cur + nums[cur]) % n:
                    break
                passed.add(cur)
                cur = (cur + nums[cur]) % n
                if cur in passed:
                    return True
