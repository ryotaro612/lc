class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        processed_source = []
        block_mode = False
        for line in source:
            processed_line = []
            i = 0
            if block_mode:
                consec = True
            else:
                consec = False
            while i < len(line):
                if not block_mode and line[i:i+2] == "/*":
                    block_mode = True
                    i += 1
                elif block_mode and line[i:i+2] == '*/':
                    block_mode = False
                    i += 1
                elif not block_mode:
                    if line[i:i+2] == '//':
                        break
                    else:
                        processed_line.append(line[i])
                
                i += 1
            
            if consec:
                processed_source[-1] = processed_source[-1] + ''.join(processed_line)
            else:
                processed_source.append(''.join(processed_line))
        
        return [l for l in processed_source if l]
