# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
[4,2,5,1,3]
3.714286
2
"""
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        if root == None or k == 0:
            return []
        order = []
        if target == root.val:
            left_num, right_num = k-1, k-1
        elif target < root.val:
            left_num,right_num = k, k-1
        else:
            left_num, right_num = k-1, k
        order.extend(self.closestKValues(root.left, target, left_num))
        order.append(root.val)
        order.extend(self.closestKValues(root.right, target, right_num))
        
        closest_dist = float('inf')
        closest_pos = -1
        n = len(order)
        for i in range(n):
            if abs(order[i] - target) < closest_dist:
                closest_dist = abs(order[i] - target)
                closest_pos = i
        
        left, right = closest_pos, closest_pos+1
        while right - left < min(k, n):
            if 0 < left:
                if right < n:
                    if abs(target - order[left-1]) < abs(target - order[right]):
                        left -=1
                    else:
                        right += 1
                else:
                    left -= 1
            else:
                right += 1
        # print(root.val, order, '->', order[left:right])
        return order[left:right]
            
        
