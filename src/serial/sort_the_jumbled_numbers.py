class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        
        return sorted(nums, key=lambda num:self.replace(mapping, num))

    def replace(self, mapping, num):
        s = str(num)
        result = []
        for c in s:
            result.append(str(mapping[ord(c) -  ord('0')]))
        return int(''.join(result))
