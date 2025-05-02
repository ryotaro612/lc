class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        result = [d for d in dominoes]
        
        updates = [i for i in range(n) if result[i] in {'R', 'L'}]

        while updates:
            next_updates= []
            for i in updates:
                if result[i] == 'L':
                    if i and result[i-1] == '.':
                        if i - 2 >= 0 and result[i-2] == 'R':
                            continue                        
                        next_updates.append([i-1, 'L'])
                else: # R
                    if i < n - 1 and result[i+1] == '.':
                        if i + 2 <= n-1 and result[i+2] == 'L':
                            continue
                        next_updates.append([i+1, 'R'])
            
            updates = []
            for i, c in next_updates:
                result[i] = c
                updates.append(i)
            
        return ''.join(result)

             


