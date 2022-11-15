class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        lst = []
        for e in arr:
            lst.append(e)
            if e == 0:
                lst.append(0)
        for i in range(len(arr)):
            arr[i] = lst[i]
