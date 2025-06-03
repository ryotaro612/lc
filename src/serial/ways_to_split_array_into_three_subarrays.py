class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        result = 0
        mod = 10**9 + 7
        n = len(nums)

        prefix = [0] * (n+1)
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]
        
        for i in range(1, n):
            lb = i
            ub = n
            while ub - lb > 1:
                mid = (lb + ub) // 2
                # [:i] [i:mid]
                if prefix[i] > prefix[mid] - prefix[i]:
                    lb = mid
                else:
                    ub = mid
            if ub == n:
                continue
            if not (prefix[i] <= prefix[ub] - prefix[i] <= prefix[n] - prefix[ub]):
                continue
            left = ub
            lb = left - 1
            ub = n
            while ub - lb > 1:
                mid = (ub + lb) // 2
                if prefix[mid] - prefix[i] > prefix[n] - prefix[mid]:
                    ub = mid
                    # print('ub', mid)
                else:
                    lb = mid
                    # print('lb', mid)
            if lb == n:
                continue
            # print(i, left, lb)
            if prefix[lb] - prefix[left] <= prefix[n] - prefix[lb]:
                result += lb - left + 1
                result %= mod

        return result                
