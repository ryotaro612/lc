class Trie:

    def __init__(self):
        self.trie = dict()

    def insert(self, word: str) -> None:
        if self.search(word):
            return
        node = self.trie
        
        for char in word:
            node[char] = node.get(char, dict())
            node = node[char]
        
        node[True] = True

    def search(self, word: str) -> bool:
        node = self.searchTail(word)
        if node is None:
            return False
        return True in node

    def startsWith(self, prefix: str) -> bool:
        return self.searchTail(prefix) is not None
        
    def searchTail(self, word: str):
        node = self.trie
        for char in word:
            if char in node:
                node = node[char]
            else:
                return None
        return node


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
