"""
["FileSystem","ls","mkdir","addContentToFile","ls","readContentFromFile"]
[[],["/"],["/a/b/c"],["/a/b/c/d","hello"],["/"],["/a/b/c/d"]]
"""
class Node:
    
    def __init__(self, name):
        self.name = name
        
    def hasName(self, name: str):
        return self.name == name
    
class File(Node):
    
    def __init__(self, name: str):
        super().__init__(name)
        self.content = ''
        
    def append(self, content: str):
        self.content += content
        
    def read(self):
        return self.content
    

class Directory(Node):
    
    def __init__(self, name):
        super().__init__(name)
        self.entries: [Node] = []
            
    
    def ls(self, subpaths: list[str]) -> Node:
        #print('dirls', self.name, subpaths)
        if subpaths == []:
            return self
        for entry in self.entries:
            if entry.hasName(subpaths[0]):
                if isinstance(entry, File):
                    return entry
                else:
                    return entry.ls(subpaths[1:])        
        assert False
        
    
    def mkdir(self, subpaths: list[str]):
        if subpaths == []:
            return
        
        name = subpaths[0]
        
        for entry in self.entries:
            if entry.hasName(name):
                entry.mkdir(subpaths[1:])
                break
        else:
            directory = Directory(name)
            directory.mkdir(subpaths[1:])
            self.entries.append(directory)
    
        
class FileSystem:

    def __init__(self):
        self.root = Directory("")

    def ls(self, path: str) -> List[str]:
        #print('ls', path)
        node = self._ls(path)
        if isinstance(node, File):
            return [node.name]
        elif isinstance(node, Directory):
            return sorted([entry.name for entry in node.entries])
    
    def mkdir(self, path: str) -> None:
        #print('mkdir', path)
        self.root.mkdir(path.split('/')[1:])

    def addContentToFile(self, filePath: str, content: str) -> None:
        #print('addcon', filePath, content)
        subpaths = filePath.split('/')
        filename = subpaths[-1]        
        if filePath.count('/') == 1:
            directory = self.root
        else:
            dirpath = '/'.join(subpaths[:-1])
            self.mkdir(dirpath)
            directory = self._ls(dirpath)
            
        for entry in directory.entries:
            if entry.hasName(filename):
                entry.append(content)
                break
        else:
            file = File(filename)
            file.append(content)
            directory.entries.append(file)
    
    def readContentFromFile(self, filePath: str) -> str:
        #print('readcontent', filePath)
        file = self._ls(filePath)
        return file.read()
        
        
    def _ls(self, path: str) -> Node:
        if path == '/':
            return self.root
        subpaths = path.split('/')
        return self.root.ls(subpaths[1:])



# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
