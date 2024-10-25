class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        found = dict()
        folder.sort()
        result = []
        for i, path in enumerate(folder):
            dirs = path.split('/')
            node = found
            skip = False
            if i:
                for directory in dirs:
                    if directory in node:
                        node = node[directory]
                    elif len(node) == 0:
                        skip = True
                        break
                    else:
                        break
            
            node = found
            if not skip:
                result.append(path)
                for directory in dirs:
                    if directory in node:
                        node = node[directory]
                    else:
                        node[directory] = dict()
                        node = node[directory]
            
        return result
