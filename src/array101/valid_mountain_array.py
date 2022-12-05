"""
[9,8,7,6,5,4,3,2,1,0]
"""
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        
        mx = max(arr)
        
        idx = [i for i, e in enumerate(arr) if e == mx]
        if len(idx) > 1 or idx[0] in {0, len(arr) - 1}:
            return False
        
        for i in range(idx[0]):
            if not arr[i] < arr[i+1]:
                return False
        
        for i in range(idx[0], len(arr)-1):
            if not arr[i] > arr[i+1]:
                return False
        
        return True
