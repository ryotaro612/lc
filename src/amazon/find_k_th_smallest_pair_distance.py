"""
[1,3,1]
1

[1,1,1]
2

[1,6,1]
3


[0,0]
1

n
O(n log n + log n^2 * (n long n) )
O(n log n + n (log n)^2
"""
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        
        lb = -1
        ub = max(nums) + 1
        
        while ub - lb > 1:
            mid = (ub + lb) // 2
            
            count = 0
            for i in range(n-1):
                idx = bisect.bisect_right(nums, nums[i] + mid, i+1)
                count += idx - i - 1
            
            if k <= count:
                ub = mid
            else:
                lb = mid
        return ub
