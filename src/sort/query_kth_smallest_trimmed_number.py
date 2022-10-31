class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        n_q = len(queries)
        
        result = []
        
        for k, trim in queries:
            trimmed = []
            for i, num in enumerate(nums):
                
                if len(num) <= trim:
                    v = num
                else:
                    v = num[-trim:]
                
                trimmed.append([v, i])
            #print(trimmed)
            trimmed = sorted(trimmed)
            result.append(trimmed[k-1][1])
        return result
    
