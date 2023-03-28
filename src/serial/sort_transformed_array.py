class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        # -b/(2*a)
        mapped = self.apply(nums, a, b, c)
        if a == 0:
            if b >=0:
                return mapped
            else:
                return mapped[::-1]
        
        if a > 0:
            v = min(mapped)
        else:
            v = max(mapped)
        for i, num in enumerate(mapped):
            if v == num:
                left = i
        l_list = mapped[:left+1]
        r_list = mapped[left+1:]

        if l_list:
            if l_list[0] < l_list[-1]:
                l_list = l_list[::-1]
        if r_list:
            if r_list[0] < r_list[-1]:
                r_list = r_list[::-1]
        result = []
        while l_list and r_list:
            if l_list[-1] < r_list[-1]:
                result.append(l_list.pop())
            else:
                result.append(r_list.pop())
        return result + l_list[::-1] + r_list[::-1]

    def apply(self, nums, a, b, c):
        return [a * v * v + b * v + c for v in nums]
