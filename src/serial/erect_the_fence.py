class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        trees.sort()
        n = len(trees)
        qs = []
        for i in range(n):
            while len(qs) > 1 and \
            self.det(self.vec(qs[-2], qs[-1]), self.vec(qs[-1], trees[i])) < 0:
                qs.pop()
            qs.append(trees[i])
        
        t = len(qs)
        for i in range(n-2, -1, -1):
            while len(qs) > t and self.det(
                self.vec(qs[-2], qs[-1]), self.vec(qs[-1], trees[i])) < 0:
                qs.pop()
            qs.append(trees[i])
        qs = {(x, y) for x, y in qs}
        return [[x, y] for x, y in qs]
    

    def det(self, xy1, xy2):
        return xy1[0] * xy2[1] - xy1[1] * xy2[0]

    def vec(self, xy1, xy2):
        return [xy2[0] - xy1[0], xy2[1] - xy1[1]]
