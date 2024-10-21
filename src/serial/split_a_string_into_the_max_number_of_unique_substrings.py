class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        counter = 0
        n = len(s)
        for i in range(1<<n):
            groups = []
            group = []
            for j in range(n):
                if j == 0:
                    group.append(s[j])
                elif (i >> j) & 1 == (i >> (j-1)) & 1:
                    group.append(s[j])
                elif i & (1<<j) == 0 and i & (1<<(j-1)) == 0:
                    group.append(s[j])
                else:
                    groups.append(''.join(group))
                    group = []
                    group.append(s[j])

            if group:
                groups.append(''.join(group))

            if len(groups) == len(set(groups)):
                counter = max(counter, len(groups))

        return counter  
