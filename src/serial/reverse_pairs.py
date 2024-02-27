import bisect

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        return self.rec(0, len(nums), nums)
    
    def rec(self, left, right, nums):
        # print('head', left, right)
        if right <= left + 1:
            return 0
        mid = (left + right) // 2
        result = self.rec(left, mid, nums) + self.rec(mid, right, nums)
        
        for j in range(mid, right):
            idx = bisect.bisect_right(nums, nums[j] * 2, left, mid)
            result += mid - idx
        
        left_i = left
        right_i = mid
        sub = []
        # print('#', left, left_i, mid, right_i)
        while left_i < mid or right_i < right:
            # print('doge', left_i, right_i)
            if right_i == right:
                sub.append(nums[left_i])
                left_i += 1
            elif left_i == mid:
                sub.append(nums[right_i])
                right_i += 1
            elif nums[left_i] < nums[right_i]:
                sub.append(nums[left_i])
                left_i += 1
            else:
                sub.append(nums[right_i])
                right_i += 1

        # print('##', left, right, sub)
        for i in range(left, right):
            nums[i] = sub[i-left]
        return result
