from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
    
        pacific = self.find_pacific(heights)
        # print(sorted(pacific))
        atlantic = self.find_atlantic(heights)
        return [[r, c] for r, c in list(pacific & atlantic)]

    def find_pacific(self, heights):
        n_row = len(heights)
        n_col = len(heights[0])
        que = deque()
        par = [-1] * (n_row * n_col)
        result = set()
        for c in range(n_col):
            self.unite(0, c, par)
            que.append([0, c])
            result.add((0, c))
        for r in range(1, n_row):
            self.unite(0, n_col * r, par)
            que.append([r, 0])
            result.add((r, 0))
    
        while que:
            r, c = que.popleft()
            for next_r, next_c in [[r-1, c], [r, c+1], [r+1, c], [r, c-1]]:
                if 0 <= next_r < n_row and 0 <= next_c < n_col and \
                  not self.is_same_group(r * n_col + c, next_r * n_col + next_c, par) and \
                  heights[r][c] <= heights[next_r][next_c]:
                    self.unite(0, next_r * n_col + next_c, par)
                    que.append([next_r, next_c])
                    result.add((next_r, next_c))
        return result

    def find_atlantic(self, heights):
        n_row = len(heights)
        n_col = len(heights[0])
        que = deque()
        par = [-1] * (n_row * n_col)
        result = set()
        group = n_row * n_col - 1
        for c in range(n_col):
            self.unite(group, n_col * (n_row - 1) + c, par)
            que.append([n_row-1, c])
            result.add((n_row-1, c))
        for r in range(n_row-1):
            self.unite(group, r * n_col + n_col - 1, par)
            que.append([r, n_col - 1])
            result.add((r, n_col - 1))
        
        while que:
            r, c = que.popleft()
            for next_r, next_c in [[r-1, c], [r, c+1], [r+1, c], [r, c-1]]:
                if 0 <= next_r < n_row and 0 <= next_c < n_col and \
                  not self.is_same_group(r * n_col + c, next_r * n_col + next_c, par) and \
                  heights[r][c] <= heights[next_r][next_c]:
                    self.unite(group, next_r * n_col + next_c, par)
                    que.append([next_r, next_c])
                    result.add((next_r, next_c))
        return result


    def find_root(self, i, par):
        if par[i] < 0:
            return i
        par[i] = self.find_root(par[i], par)
        return par[i]
    
    def is_same_group(self, a, b, par):
        return self.find_root(a, par) == self.find_root(b, par)

    def unite(self, a, b, par):
        if self.is_same_group(a, b, par):
            return
        root_a = self.find_root(a, par)
        root_b = self.find_root(b, par)
        if par[root_a] < par[root_b]:
            par[root_a] += par[root_b]
            par[root_b] = root_a
        else:
            par[root_b] += par[root_a]
            par[root_a] = root_b
