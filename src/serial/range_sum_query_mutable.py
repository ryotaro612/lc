class NumArray:

    def __init__(self, nums: List[int]):
        self.bit = [0] * (len(nums) + 1)
        for i, num in enumerate(nums):
            self._add(i, num)

    def update(self, index: int, val: int) -> None:
        v = self._sum(index+1) - self._sum(index)
        self._add(index, val-v)

    def sumRange(self, left: int, right: int) -> int:
        return self._sum(right+1) - self._sum(left)
    
    def _add(self, i, v):
        i+= 1
        while i < len(self.bit):
            self.bit[i] += v
            i += i & -i
    
    def _sum(self, i):
        result = 0
        while i:
            result += self.bit[i]
            i -= i & -i
        return result
