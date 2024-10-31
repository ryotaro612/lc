class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        current = [[' '] * 3 for _ in range(3)]
        for r in range(3):
            for c in range(3):
                if self.rec(current, board, True):
                    return True
        return False

    def rec(self, current, board, turn):
        ok = True
        cells = []
        for r in range(3):
            for c in range(3):
                ok = ok and current[r][c] == board[r][c]
                if current[r][c] == ' ':
                    cells.append([r, c])
                elif current[r][c] != board[r][c]:
                    return False
        if ok:
            return True
        
        if not cells:
            return False
        # print(current)
        cands = []
        for i in range(3):
            row = set([current[0][i], current[1][i], current[2][i]])
            diag = set([current[0][0], current[1][1], current[2][2]])
            rev_diag = set([current[0][2], current[1][1], current[2][0]])
            cands.extend([set(current[i]), row, diag, rev_diag])
        for cand in cands:
            if cand == {'O'} or cand == {'X'}:
                return False
        for r, c in cells:
            current[r][c] = 'X' if turn else 'O'
            if self.rec(current, board, not turn):
                return True
            current[r][c] = ' '
        return False
