"""
4
[1,0,3,-1]
[-1,-1,-1,-1]
"""
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        root = -1
        children = set(leftChild + rightChild)
        for i in range(n):
            if i not in children:
                root = i
        if root == -1:
            return False
        
        visit = [False] * n
        visit[root] = True
        if not self.traverse(root, visit, leftChild, rightChild):
            return False
        return n == len([v for v in visit if v])
    
    def traverse(self, node, visit, leftChild, rightChild):
        result = True
        for children in [leftChild, rightChild]:
            if children[node] >= 0:
                if visit[children[node]]:
                    return False
                visit[children[node]] = True
                result = result and self.traverse(children[node], visit, leftChild, rightChild)
        return result
