class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:

        self.putNumber(0, 0, board)
        
    def putNumber(self, r, c, board):
        if board[r][c] != '.':
            if r == 8 and c == 8:
                return True
            else:
                next_r, next_c = self.next_pos(r, c)
                return self.putNumber(next_r, next_c, board)
        else:
            nums = {str(i) for i in range(1, 10)}
            for i in range(9):
                if c != i and board[r][i] in nums:
                    nums.remove(board[r][i])
                if r != i and board[i][c] in nums:
                    nums.remove(board[i][c])
            for base_r in [6, 3, 0]:
                if base_r == min(base_r, r):
                    break
            for base_c in [6, 3, 0]:
                if base_c == min(base_c, c):
                    break
            
            for i in range(base_r, base_r + 3):
                for j in range(base_c, base_c + 3):
                    if r != i and c != j and board[i][j] in nums:
                        nums.remove(board[i][j])

            for num in nums:
                board[r][c] = num
                if r == 8 and c == 8:
                    return True
                else:
                    next_r, next_c = self.next_pos(r, c)
                    if self.putNumber(next_r, next_c, board):
                        return True
                    else:
                        board[r][c] = '.'
            return False
    
    def isValid(self, r, c, board):
        if r == 8:
            nums =set()
            for i in range(9):
                nums.add(board[i][c])
            if len(nums) < 9:
                return False
        if r in {2, 5, 8} and c in {2, 5, 8}:
            nums = set()
            for i in range(r-2, r+1):
                for j in range(c-2, c+1):
                    nums.add(board[i][j])
            if len(nums) < 9:
                return False
        return True
    def next_pos(self, r, c):
        if c < 8:
            return r, c+1
        elif r < 8:
            return r+1, 0
        return None
        
