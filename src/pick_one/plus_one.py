class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = list(digits)
        n = len(result)
        for index in range(n)[::-1]:
            if result[index] == 9:
                result[index] = 0
                if index == 0:
                    return [1] + result
            else:
                result[index] += 1
                return result
