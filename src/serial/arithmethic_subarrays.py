class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        result = []
        n_queries = len(l)
        for left, right in zip(l, r):
            sub = sorted(nums[left:right+1])

            n_sub = len(sub)
            ok = True

            for i in range(1, n_sub):
                ok = ok and sub[i] - sub[i-1] == sub[1] - sub[0]

            result.append(ok)

        return result
