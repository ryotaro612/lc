class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        return self.rec([c for c in password])
    def rec(self, password):
        #print(len(password), ''.join(password))
        lower = []
        upper = []
        digit = []
        repeats = []
        symbols = []
        n = len(password)
        for i, c in enumerate(password):
            if c.islower():
                lower.append(i)
            elif c.isupper():
                upper.append(i)
            elif c.isdigit():
                digit.append(i)
            else:
                symbols.append(i)
            if i < n-2 and password[i] == password[i+1] == password[i+2]:
                repeats.append(i+2)

        
            
        if 6 <= n <= 20 and lower and upper and digit and not repeats:
            return 0
        
        if n <= 2:
            return 6 - n
        if n < 6:
            if repeats:
                symbol = None
                if not lower:
                    symbol = 'a'
                if not upper:
                    symbol = 'A'
                if not digit:
                    symbol = '0'
                if symbol is not None:
                    password.insert(repeats[0], symbol)
                    return 1 + self.rec(password)
                for c in 'abc':
                    i = repeats[0]
                    if password[i-1] != c and (i == n-1 or password[i+1] != c):
                        password.insert(i, c)
                        return 1 + self.rec(password)
            if not lower:
                password.append('a')
                return 1 + self.rec(password) 
            if not upper:
                password.append('A')
                return 1 + self.rec(password)
            if not digit:
                password.append('0')
                return 1 + self.rec(password)
            return 6 - n

        if n <= 20:
            if repeats:
                if not lower:
                    password[repeats[0]] = 'a'
                    return 1 + self.rec(password)
                if not upper:
                    password[repeats[0]] = 'A'
                    return 1 + self.rec(password)
                if not digit:
                    password[repeats[0]] = '0'
                    return 1 + self.rec(password)
                for c in 'abc':
                    i = repeats[0]
                    if password[i-1] != c and (i == n-1 or password[i+1] != c):
                        password[i] = c
                        return 1 + self.rec(password)
            return len([v for v in [lower, upper, digit] if not v])

        if repeats:
            left = 0
            patterns = [[], [], []]
            for right in range(2, n):
                if password[right-2] == password[right-1] == password[right]:
                    if right == n -1 or password[right] != password[right+1]:
                        #print(left, right)
                        patterns[(right - left + 1)%3].append(left)
                elif password[right-1] == password[right]:
                    left = right-1
                else:
                    left = right
            #print(patterns)
            for pattern in patterns:
                if pattern:
                    pos = pattern[0]+2
                    return 1 + self.rec(password[:pos] + password[pos+1:])
        
        max_len = max([len(l) for l in [lower, upper, digit, symbols]])
        for seq in [lower, upper, digit, symbols]:
            if max_len == len(seq):
                i = seq[0]
                return 1 + self.rec(password[:i] + password[i+1:])
        
