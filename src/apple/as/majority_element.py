"""
[4,2,1,1]

[2,1,1,3,1,4,5,6]
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if nums == []:
            return []
        
        candidate1, candidate2 = None, None
        freq1, freq2 = 0, 0
        
        for v in nums:
            if candidate1 == v:
                freq1 += 1
            elif candidate2 == v:
                freq2 += 1
            elif freq1 == 0:
                candidate1 = v
                freq1 = 1
            elif freq2 == 0:
                candidate2 = v
                freq2 = 1
            else:
                freq1 -= 1
                freq2 -= 1
        result = []
        
        for candidate in [candidate1, candidate2]:

            if candidate is None:
                continue
            
            freq = 0
            for v in nums:
                if candidate == v:
                    freq += 1
            
            if freq > len(nums) // 3:
                result.append(candidate)
        return result
                
                    
