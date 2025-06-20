class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        trie = dict()
        n = len(arr)
        for i in range(n):
            n_w = len(arr[i])
            for start in range(n_w):
                cur = trie
                for j in range(start, n_w):
                    c = arr[i][j]
                    if c in cur:
                        cur[c][0].add(i)
                    else:
                        cur[c] = [{i}, dict()]
                    cur = cur[c][1]
        result = [""] * n
        for i in range(n):
            n_w = len(arr[i])
            for start in range(n_w):
                for end in range(start, n_w+1):
                    cur = trie
                    sub = arr[i][start:end]
                    for c in sub:
                        if len(cur[c][0]) == 1:
                            if result[i]:
                                if len(result[i]) > len(sub):
                                    result[i] = sub
                                elif len(result[i]) == len(sub):
                                    result[i] = min(sub, result[i])
                            else:
                                result[i] = sub
                            break
                        else:
                            cur = cur[c][1]
            # result.append(item if item else "")
        
        return result
