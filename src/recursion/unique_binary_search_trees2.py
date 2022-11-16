# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        return self.buildTrees([i for i in range(1, n+1)])
    
    def buildTrees(self, nodes):
        if len(nodes) == 0:
            return [None]
        
        result = []
        
        for node in nodes:
            left = [child for child in nodes if child < node]
            right = [child for child in nodes if node < child]
            
            left_trees = self.buildTrees(left)
            right_trees = self.buildTrees(right)
            
            for left_tree in left_trees:
                for right_tree in right_trees:
                    result.append(TreeNode(node, left_tree, right_tree))
        
        return result
