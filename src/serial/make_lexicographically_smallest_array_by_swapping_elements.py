import heapq

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)

        ordered = [(num, i) for i, num in enumerate(nums)]
        ordered.sort()

        right = 0
        result = [0] * n
        i = 0
        while i < n:
            index = [ordered[i][1]]
            values = [ordered[i][0]]
            
            while i < n - 1 and ordered[i+1][0] - ordered[i][0] <= limit:
                index.append(ordered[i+1][1])
                values.append(ordered[i+1][0])
                i += 1
            
            for a, v in zip(sorted(index), sorted(values)):
                result[a] = v
            
            i += 1
            

        return result
