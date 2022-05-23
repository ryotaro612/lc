class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        """
        first  second
        [3 5]  [6 7] => move left poitner
        [3 6]  [4 5] => move right pointer
        [3 6]  [4 7] => move left pointer
        [3 6]  [1 5] => move right pointer
        [3 6]  [1 2] => move right pointer
        """
        result = []
        i, j = 0, 0
        while i < len(firstList) and j < len(secondList):
            first, second = firstList[i], secondList[j]
            # int(first, second)
            if first[1] < second[0]:
                i += 1
                continue
            if first[0] > second[1]:
                j += 1
                continue
            # print('doge')
            l = max(first[0], second[0])
            r = min(first[1], second[1])
            if len(result) > 0 and result[-1][1] == l:
                result[-1] = [result[-1][0], r]
            else:
                result.append([l, r])
            if first[1] < second[1]:
                i += 1
            else:
                j += 1
        return result
        
