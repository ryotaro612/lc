from collections import Counter
class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        counter1 = Counter(nums1)
        counter2 = Counter(nums2)

        n = len(nums1)

        s = set()
        n_selected1 = 0
        for num in counter1:
            if num not in counter2 and n_selected1 < n // 2:
                s.add(num)
                counter1[num] -= 1
                n_selected1 += 1
        
        n_selected2 = 0
        for num in counter2:
            if num not in counter1 and n_selected2 < n // 2:
                s.add(num)
                n_selected2 += 1
                counter2[num] -= 1
        
        for num in counter1:
            if num not in s and counter1[num] and n_selected1 < n // 2:
                s.add(num)
                counter1[num] -= 1
                n_selected1 += 1
        
        for num in counter2:
            if num not in s and counter2[num] and n_selected2 < n // 2:
                s.add(num)
                n_selected2 += 1
                counter2[num] -= 1
        
        return len(s)
