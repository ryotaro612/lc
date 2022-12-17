class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        e = -float('inf')
        n = len(arr)
        for i in range(n-1, -1, -1):
            if i == n -1:
                e = arr[i]
                arr[i] = -1
            else:
                temp = arr[i]
                arr[i] = e
                e = max(e, temp)
        return arr
