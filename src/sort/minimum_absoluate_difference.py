class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr = sorted(arr)
        n = len(arr)
        mini = float('inf')
        
        for i in range(n-1):
            mini = min(mini, arr[i+1] - arr[i])
        
        result = []
        for i in range(n-1):
            if mini == arr[i+1] - arr[i]:
                result.append([arr[i], arr[i+1]])
        return result
