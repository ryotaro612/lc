class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        alice = 0
        bob = 0
        n = len(colors)
        for i, c in enumerate(colors):
            if i and i < n - 1:
                if colors[i-1] == c == colors[i+1]:
                    if c == 'A':
                        alice += 1
                    else:
                        bob += 1
        return alice > bob
