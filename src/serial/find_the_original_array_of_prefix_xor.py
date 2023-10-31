class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        
        result = [pref[0]]
        acc = result[0]
        for i in range(1, len(pref)):
            v = acc ^ pref[i]
            result.append(v)
            acc ^= v
        return result
