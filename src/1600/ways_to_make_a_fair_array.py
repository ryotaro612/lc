class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        """
        odd[i] = nums[1] + nums[3] + .... + nums[i] if i is odd nums[i-1]
        even[i] = nums[0] + nums[2] + ... + nums[i] if i is even nums[i-1]
        """
        n = len(nums)
        odd = [0] * n
        even = [0] * n
        for i in range(n):
            if i == 0:
                even[0] = nums[0]
            else:
                if i % 2:
                    odd[i] = nums[i]
                else:
                    even[i] = nums[i]

                odd[i] += odd[i-1]
                even[i] += even[i-1]
        
        result = 0
        for i in range(n):
            if i == 0:
                total_even = odd[n-1]
                total_odd = even[n-1] - nums[0]
            else:
                if i % 2:
                    total_even = even[i]
                    total_even += odd[n-1] - odd[i]
    
                    total_odd = odd[i-1]
                    total_odd += even[n-1] - even[i]
                else:
                    total_even = even[i-1]
                    total_even += odd[n-1] - odd[i]
                    total_odd = odd[i]
                    total_odd += even[n-1] - even[i]
            
            if total_even == total_odd:
                result += 1

        return result
