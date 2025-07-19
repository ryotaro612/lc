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
"""
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        """
        """
        result = []
        folder.sort()
        trie = [dict(), False]

        for path in folder:
            nodes = [node for node in path.split('/') if node]

            cur = trie
            ok = True
            for node in nodes:
                if node in cur[0]:
                    cur = cur[0][node]
                    if cur[1]:
                        ok = False
                        break
                else:
                    break
            if ok:
                result.append(path)

            cur = trie
            for node in nodes:
                if node in cur[0]:
                    cur = cur[0][node]
                else:
                    cur[0][node] = [dict(), False]
                    cur = cur[0][node]
            cur[1] = True

        return result


"""
