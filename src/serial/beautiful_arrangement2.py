class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        """
        10
        4
        """
        result = []
        m = n
        while k < m:
            result.append(m)
            m -= 1
        
        a = 1
        # print(result, k, m)
        while len(result) < n:
            result.append(a)
            a += 1
            if len(result) < n:
                result.append(m)
                m -= 1
        return result
