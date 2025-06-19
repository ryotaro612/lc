class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        
        nums.sort()

        partitions = self.divide(nums, k)
        rev_partitions = self.divide(nums[::-1], k)

        return min(len(partitions), len(rev_partitions))

    
    def divide(self, nums, k):

        result = []

        n = len(nums)
        cur = []
        for num in nums:
            if cur:
                if abs(cur[0] - num) <= k:
                    cur.append(num)
                    continue
                result.append(cur)
                cur = [num]
                continue

            cur = [num]
        
        result.append(cur)
        return result
