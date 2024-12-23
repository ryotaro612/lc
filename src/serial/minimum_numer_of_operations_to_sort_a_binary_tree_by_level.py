from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        depths = defaultdict(list)

        self.traverse(root, 0, depths)
        result = 0 
        for k in depths:
            counter = 0
            remap = dict()
            for node in sorted(depths[k]):
                remap[node] = counter
                counter += 1

            result += self.count([remap[node] for node in depths[k]])
        return result
    
    def count(self, nodes):
        val_pos = dict()
        for i, node in enumerate(nodes):
            val_pos[node] = i
        
        res = 0
        n = len(nodes)
        for i in range(n):
            if i == nodes[i]:
                continue
            
            pos = val_pos[i]
            res += 1
            temp = nodes[i]
            nodes[i], nodes[pos] = i, nodes[i]
            val_pos[i] = i
            val_pos[temp] = pos
        
        return res

    
    def traverse(self, node, depth, depths):
        if node is None:
            return
        
        depths[depth].append(node.val - 1)
        for child in [node.left, node.right]:
            self.traverse(child, depth+1, depths)
