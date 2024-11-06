class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        result = []
        chunk = []

        for num in nums:
            if chunk:
                if self.count(chunk[-1]) == self.count(num):
                    chunk.append(num)
                else:
                    chunk.sort()
                    result.extend(chunk)
                    chunk = [num]
            else:
                chunk.append(num)
        
        chunk.sort()
        result.extend(chunk)
        return result == sorted(result)
    
    def count(self, num):
        counter = 0
        while num:
            if num & 1:
                counter += 1
            num >>= 1
        return counter
