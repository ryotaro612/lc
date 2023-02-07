"""
[0,0,0,0,0]
[80387,68178,55969,31551]
"""
class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        n = len(arr)
        diff = arr[1] - arr[0]
        #print(diff)
        if abs(diff) > abs(arr[2] - arr[1]):
            return arr[0] + arr[2] - arr[1]
        for i in range(1, n-1):
            print(arr[i+1]-arr[i])
            if abs(diff) < abs(arr[i+1] - arr[i]):
                return arr[i] + diff
        return arr[0]
