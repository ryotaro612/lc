class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        for i in range(n):
            freq_row = [0] * 10
            freq_col = [0] * 10
            for j in range(n):
                if board[i][j] != '.':
                    num = int(board[i][j])
                    freq_row[num] += 1
                    if 1 < freq_row[num]:
                        return False
                if board[j][i] != '.':
                    num = int(board[j][i])
                    freq_col[num] += 1
                    if 1 < freq_col[num]:
                        return False
        for i in range(0, n, 3):
            for j in range(0, n, 3):
                freq = [0] * 10
                for r in range(3):
                    for c in range(3):
                        if board[i+r][j+c] != '.':
                            num = int(board[i+r][j+c])
                            freq[num] += 1
                            if 1 < freq[num]:
                                return False
        return True
