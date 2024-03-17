class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        n_rows = len(board)
        n_cols = len(board[0])

        r, c = click

        if board[r][c] == 'M':
            board[r][c] = 'X'
            return board
        
        neighbors = []
        n_mines = 0
        for n_r, n_c in [[y, x] for x in range(c-1, c+2) for y in range(r-1, r+2)]:       
            if not (n_r == r and c == n_c) and 0 <= n_r < n_rows and 0 <= n_c < n_cols:
                if board[n_r][n_c] in {'M', 'E'}:
                    neighbors.append([n_r, n_c])
                    if board[n_r][n_c] == 'M':
                        n_mines += 1
        
        if n_mines == 0:
            board[r][c] = 'B'
            for n_r, n_c in neighbors:
                self.updateBoard(board, [n_r, n_c])
        else:
            board[r][c] = str(n_mines)

        return board
    
