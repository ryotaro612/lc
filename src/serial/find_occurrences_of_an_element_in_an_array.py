class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        """
        occur[queries[i]-1]
        queries[i]

        result = []
        n = len(nums)
        
        """
        occur = [i for i, num in enumerate(nums) if num == x]
        result = []
        for query in queries:
            if query - 1 < len(occur):
                result.append(occur[query-1])
            else:
                result.append(-1)
        return result

