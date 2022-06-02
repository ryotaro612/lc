class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counter = dict()
        for cpdomain in cpdomains:
            cp, domain = cpdomain.split(' ')
            cp = int(cp)
            subs = domain.split('.')
            for i in range(len(subs)):
                key = '.'.join(subs[i:])
                if key not in counter:
                    counter[key] = 0
                counter[key] += cp
        return [str(v) + " " + k for k, v in counter.items()]
