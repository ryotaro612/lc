# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        cands = [root]
        delete_set = set(to_delete)
        self.drop(root, cands, delete_set)
        return [cand for cand in cands if cand.val not in delete_set]

    def drop(self, node, cands, delete_set):
        if node.left:
            self.drop(node.left, cands, delete_set)      
            if node.left.val in delete_set:
                node.left = None
            elif node.val in delete_set:
                cands.append(node.left)

        if node.right:
            self.drop(node.right, cands, delete_set)
            if node.right.val in delete_set:
                node.right =  None
            elif node.val in delete_set:
                cands.append(node.right)
            
