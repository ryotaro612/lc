
class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
      n = len(nums)
      prev = nums[-1]
      result = 0
      for i in range(n-2,-1,-1):
        # print(i, prev, nums[i])
        if nums[i] <= prev:
          prev = nums[i]
          continue
        elif nums[i] % prev == 0:
          result += nums[i] // prev - 1
          continue
        else:
          n_div = nums[i] // prev + 1
          lb = 0
          ub = prev + 1
          while ub - lb > 1:
            mid = (ub +lb) // 2
            if mid * n_div > nums[i]:
              ub = mid
            else:
              lb = mid
          result += n_div - 1
          prev = lb
      return result
