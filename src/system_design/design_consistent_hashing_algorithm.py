"""
hash(int) -> str
nodes = sorted([(hashed_node_id, node_id), ...])


hashed_key = hash(key)
"""
import hashlib
import bisect

class ConsistentHashing:

    def __init__(self, initialNodes: int):
        self.max_node_id = initialNodes
        self.nodes = sorted([(self.hash(node_id), node_id, set()) 
                             for node_id 
                             in range(1, initialNodes + 1)])
        
    def getNodeForKey(self, key: int) -> int:
        _, node_id, keys = self.nodes[self.findNextNode(key)]
        keys.add(key)
        return node_id

    def removeNode(self, node: int) -> int:
        for i, (hash_node_id, node_id, keys) in enumerate(self.nodes):
            if node == node_id:
                self.nodes.pop(i)
                _, next_node_id, next_keys = self.nodes[self.findNextNode(node)]
                next_keys.update(keys)
                return next_node_id
        
        raise RuntimeError('unreachable')
        
    def addNode(self) -> List[int]:
        self.max_node_id += 1
        node_id = self.max_node_id
        next_node_idx = self.findNextNode(node_id)
        next_node_id = self.nodes[next_node_idx][1]
        self.nodes.append((self.hash(node_id), node_id, set(self.nodes[next_node_idx][2])))
        self.nodes.sort()
        return [node_id, next_node_id]

    def getKeysInNode(self, node: int) -> List[int]:
        hash_key = self.hash(node)
        idx = bisect.bisect_left(self.nodes, hash_key, key=lambda t: t[0])
        return list(self.nodes[idx][2])
    
    def findNextNode(self, key: int):
        node_idx = bisect.bisect_left(
            self.nodes, self.hash(key), key=lambda t: t[0])
        
        if len(self.nodes) == node_idx:
            node_idx = 0
        
        return node_idx
    
    def hash(self, i: int):
        return hashlib.sha256(str(i).encode()).hexdigest()
    
# hashlib.sha256('1'.encode()).hexdigest()
# Your ConsistentHashing object will be instantiated and called as such:
# obj = ConsistentHashing(initialNodes)
# param_1 = obj.getNodeForKey(key)
# param_2 = obj.removeNode(node)
# param_3 = obj.addNode()
# param_4 = obj.getKeysInNode(node)
