# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:

        child_to_parent = {root.val: None}
        self.associate_parent(root, child_to_parent)        
        start = self.find_node(root, startValue)
        directions = []
        self.find_path(start, destValue, child_to_parent, set(), directions)
        return ''.join(directions)

    def find_path(self, node, dest_val, child_to_parent, passed, directions):
        if node is None:
            return False
        if node.val == dest_val:
            return True

        neighbors = [[child_to_parent[node.val], 'U'], [node.left, 'L'], [node.right, 'R']]
        passed.add(node.val)
        for neighbor, direction in neighbors:
            if neighbor is None or neighbor.val in passed:
                continue
            directions.append(direction)
            if self.find_path(neighbor, dest_val, child_to_parent, passed, directions):
                return True
            directions.pop()

    def find_node(self, node, val):
        if node is None:
            return
        if node.val == val:
            return node
        for child in [node.left, node.right]:
            found = self.find_node(child, val)
            if found:
                return found

    def associate_parent(self, node, child_to_parent):
        for child in [node.left , node.right]:
            if child:
                child_to_parent[child.val] = node
                self.associate_parent(child, child_to_parent)
