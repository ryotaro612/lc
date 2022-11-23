class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        n = len(arr)
        
        for i in range(n-1):
            for j in range(i+1, n):
                if arr[i] == 2 * arr[j] or arr[i] * 2 == arr[j]:
                    return True
        
        return False
