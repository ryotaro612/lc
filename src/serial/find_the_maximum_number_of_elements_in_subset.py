from collections import Counter
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        result = 0

        counter = Counter(nums)

        for num in nums:
            if num == 1:
                if counter[num] % 2:
                    result = max(result, counter[num])
                else:
                    result = max(result, counter[num]-1)
                continue

            temp = 0
            v = num

            while v in counter:
                if v * v in counter:
                    if counter[v] == 1:
                        temp += 1
                        break
                    else:
                        temp += 2
                else:
                    temp += 1
                v *= v 
            
            result = max(result, temp)
        
        return result


        """
        coutner

        result = 0
        counter[num] == 1

        num ** 2 ** 2
        result = 2
        num == 1
        counter[num] - 1
        """
