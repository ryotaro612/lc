class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        n_row = len(board)
        n_col = len(board[0])
        result = 0
        for r in range(n_row):
            for c in range(n_col):
                if board[r][c] == 'X':
                    for d_r, d_c in [[-1, 0], [0, 1], [1, 0], [0, -1]]: 
                        if 0 <= r + d_r < n_row and 0 <= c + d_c < n_col and board[r + d_r][c + d_c] == 'X':
                            peek_r = r
                            peek_c = c
                            while 0 <= peek_r < n_row and 0 <= peek_c < n_col and board[peek_r][peek_c] == 'X':
                                board[peek_r][peek_c] = '.'
                                peek_r += d_r
                                peek_c += d_c
                            
                            result += 1
                            break
                    else:
                        board[r][c] = '.'
                        result += 1
        return result
                            
