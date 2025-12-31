from collections import defaultdict

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        """
        nums1[i] // k

        counter[] <- factor of new array
        result = 0
        result += counter[nums2[i]]
        """
        counter = defaultdict(int)

        for e in [e//k for e in nums1 if e % k == 0]:
            for f in self.find_factors(e):
                counter[f] += 1
        
        result = 0
        for num in nums2:
            result += counter[num]
        return result

    def find_factors(self, num):
        v = 1
        factors = []
        while v * v <= num:
            if num % v == 0:
                factors.append(v)
                if v != num // v:
                    factors.append(num // v)
            v += 1
        return factors
