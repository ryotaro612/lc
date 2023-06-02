class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        for i in range(1 << 9):
            selected = []
            for j in range(9):
                if i & (1 << j):
                    selected.append(j + 1)
            if sum(selected) == n and len(selected) == k:
                result.append(selected)
        return result


"""
9
45
"""
"""
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
    
        result = []

        self.search(1, [], 0, k, n, result)
        return result

    def search(self, v, temp, total, k, n, result):
        
        if total == n and len(temp) == k:
            result.append(list(temp))
            return

        if total > n or v > 9 or len(temp) > k:
            return
        
        temp.append(v)
        self.search(v+1, temp, total + v, k, n, result)
        temp.pop()
        self.search(v+1, temp, total, k, n, result)
"""
