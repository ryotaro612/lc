class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if self.is_ipv4(queryIP):
            return 'IPv4'
        elif self.is_ipv6(queryIP):
            return 'IPv6'
        else:
            return 'Neither'
    
    def is_ipv4(self, ip):
        if 27 < len(ip):
            return False
        x_list = ip.split('.')
        if len(x_list) != 4:
            return False
        
        digits = set([str(i) for i in range(10)])
        for x in x_list:
            if len(x) == 0:
                return False
            for c in x:
                if c not in digits:
                    return False
            if x[0] == '0' and len(x) > 1:
                return False
            v = int(x)
            if not (0<= v and v <= 255):
                return False
        return True
    
    def is_ipv6(self, ip):
        if 39 < len(ip):
            return False
        
        x_list = ip.split(':')
        if len(x_list) != 8:
            return False
        
        letters = set([str(i) for i in range(10)] + ['a', 'b', 'c', 'd', 'e', 'f'] + ['A', 'B', 'C', 'D', 'E', 'F'])
        for x in x_list:
            if not (0 < len(x) and len(x) <= 4):
                return False
            for c in x:
                if c not in letters:
                    return False
        return True
    
