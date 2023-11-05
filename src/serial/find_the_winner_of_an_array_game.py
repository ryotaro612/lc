class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        front = arr[0]
        count = 0
        for i in range(1, len(arr)):
            if front < arr[i]:
                count = 1
                front = arr[i]
            else:
                count += 1
            if count == k:
                return front
        return max(arr)
