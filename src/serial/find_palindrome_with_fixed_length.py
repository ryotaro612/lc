class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        """
        """
        # return []
        res = []
        for item in queries:
            # print('item', item)
            res.append(self.solve(item, intLength))
            # print('res', res[-1])
            # print('')
        return res

    def solve(self, target, length):
        # print('target', target)
        if length == 1:
            if target <= 9:
                return target
            return -1
        
        if length % 2:
            digits = (length - 1) // 2 + 1
        else:
            digits = length // 2
        
        digits -= 1
        if target > 9 * (10**digits):
            return -1

        res = []
        for i in range(1, 10):
            if target <= 10**digits:
                res.append(i)
                break
            else:
                target -= 10**digits
            
        for d in range(digits-1, -1, -1):
            for i in range(10):
                if target <= 10**d:
                    res.append(i)
                    break
                else:
                    target -= 10**d

        # print('res', res)          
        txt = ''.join(str(c) for c in res)
        if length % 2:
            return int(txt + txt[:-1][::-1])
        else:
            return int(txt + txt[::-1])
