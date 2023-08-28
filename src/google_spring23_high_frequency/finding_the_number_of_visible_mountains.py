class Solution:
    def visibleMountains(self, peaks: List[List[int]]) -> int:
        peaks = sorted(peaks)
        n = len(peaks)
        visible = [True] * n
        t_l, t_r = [-float('inf')] * 2
        for i in range(n):
            x, y = peaks[i]
            if y + x <= t_l:
                visible[i] = False
            t_l = max(t_l, y+x)
            
            x, y = peaks[n-1-i]
            if y - x <= t_r:
                visible[n-1-i] = False
            t_r = max(t_r, y -x)
        return len([v for v in visible if v])
