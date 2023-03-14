class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        s_set = set(source)
        if not all(c in s_set for c in target):
            return -1
        n_source = len(source)
        n_target = len(target)
        result = 0
        s_pos, t_pos = 0, 0
        while t_pos < n_target:
            if s_pos == 0:
                result += 1
            if source[s_pos] == target[t_pos]:
                t_pos += 1
            s_pos = (s_pos + 1) % n_source
        return result
