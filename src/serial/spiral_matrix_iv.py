# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        dir_i = 0
        pos_r, pos_c = 0, 0

        grid = [[-1] * n for _ in range(m)]

        while head:
            grid[pos_r][pos_c] = head.val
            head = head.next

            n_r = pos_r + direction[dir_i][0]
            n_c = pos_c + direction[dir_i][1]  
            if 0 <= n_r < m and 0 <= n_c < n and grid[n_r][n_c] == -1:
                pos_r = n_r
                pos_c = n_c
            else:
                dir_i = (dir_i + 1) % 4
                pos_r += direction[dir_i][0]
                pos_c += direction[dir_i][1]
        
        return grid
