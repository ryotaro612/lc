class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        result = 0
        mini, mx = arrays[0][0], arrays[0][-1]

        for i in range(1, len(arrays)):
            arr = arrays[i]
            result = max(result, abs(arr[0] - mx), abs(arr[-1] - mini))
            mini = min(mini, arr[0])
            mx = max(mx, arr[-1])

        return result
