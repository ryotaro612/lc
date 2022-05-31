class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = dict()
        for product in products:
            self.add(trie, product)
        result = [[] for _ in range(len(searchWord))]
        ## from
        for i in range(len(searchWord)):
            c = searchWord[i]
            if c in trie:
                trie = trie[c]
                self.search(trie, result[i])
            else:
                break
                
        return result
    
    def search(self, trie, result):
        if len(result) == 3:
            return
        if '' in trie:
            result.append(trie[''])
        if len(result) == 3:
            return
        for c in [chr(ord('a') + i) for i in range(26)]:
            if c in trie:
                self.search(trie[c], result)
        
    def add(self, trie, product):
        node = trie
        n = len(product)
        
        for i, c in enumerate(product):
            node.setdefault(c, dict())
            node = node[c]
            if i == n - 1:
                node[''] = product
