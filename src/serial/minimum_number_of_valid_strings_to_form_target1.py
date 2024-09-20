class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:

        trie = dict()
        for word in words:
            node = trie
            for c in word:
                if c not in node:
                    node[c] = dict()
                node = node[c]

        n_target = len(target)
        dp = [float('inf')] * (n_target + 1)
        dp[0] = 0

        for i in range(n_target):
            node = trie
            j = 0
            while i + j < n_target and target[i+j] in node:
                dp[i+j+1] = min(dp[i+j+1], dp[i] + 1)
                node = node[target[i+j]]
                j += 1

        return dp[n_target] if dp[n_target] < float('inf') else -1
