"""
["zkiikgv","zkiikgv","zkiikgv","zkiikgv"]
[436363475,710406388,386655081,797150921]
["wnaaxbfhxp","mryxsjc","oz","wlarkzzqht"]
"""
from collections import defaultdict

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        n = len(username)
        triples = sorted([(u, t, w) for u, t, w in zip(username, timestamp, website)], key=lambda triple: triple[1])

        user_sites = defaultdict(list)
        for u, _, w in triples:
            user_sites[u].append(w)

        pattern_users = defaultdict(set)
        # print(user_sites)
        for user, websites in user_sites.items():
            n_websites = len(websites)
            for i in range(n_websites-2):
                for j in range(i+1, n_websites-1):
                    for k in range(j+1, n_websites):
                        pattern_users[(websites[i], websites[j], websites[k])].add(user)
        
        # print(pattern_users)
        max_score = max([len(l) for l in pattern_users.values()])

        candidates = []
        for pattern, users in pattern_users.items():
            if len(users) == max_score:
                candidates.append(pattern)
        # print(candidates)
        result = sorted(candidates)[0]
        return result
