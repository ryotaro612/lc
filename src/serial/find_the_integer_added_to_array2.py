from collections import Counter
class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        """
        a1 = [(v, freq)] # nums1
        a2 = #nums2

        a1[i][0] a2[i][0] +x
        result 
        """
        counter1 = Counter(nums1)
        counter2 = Counter(nums2)
        mini2 = min(nums2)
        n = len(nums1)
        result = float('inf')
        for i in range(n):
            """
            num1 + x = num2
            """
            x = mini2 - nums1[i]
            ok = True
            temp1 = dict(counter1)
            for num, f in counter2.items():
                if  counter2[num] > temp1.get(num - x, 0):
                    ok = False
                    break
                else:
                    temp1[num-x] -= counter2[num]
            
            if ok and sum(temp1.values()) == 2:
                result = min(result, x)
        
        return result
