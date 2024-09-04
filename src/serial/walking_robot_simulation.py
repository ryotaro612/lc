class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        r, c = 0, 0

        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        result = 0
        obstacles = {tuple(o) for o in obstacles}
        
        i = 0
        for command in commands:
            # print(r, c, i)
            if command == -2:
                i = (i + 4 - 1) % 4
                continue
            elif command == -1:
                i = (i + 1) % 4
                continue
            
            for _ in range(command):

                n_r, n_c = (r + direction[i][0], c + direction[i][1])
                if (n_r, n_c) in obstacles:
                    break
            
                r, c = n_r, n_c
                result = max(result, n_r**2 + n_c**2)
        
            
        return result
