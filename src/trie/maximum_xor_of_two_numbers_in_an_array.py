class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        root = dict()
        
        for num in nums:
            node = root
            for i in range(30, -1, -1):
                if num & (1 << i):
                    node[1] = node.get(1, dict())
                    node = node[1]
                else:
                    node[0] = node.get(0, dict())
                    node = node[0]
        result = 0
        
        for num in nums:    
            temp = 0
            node = root
            # print(num)
            for i in range(30, -1, -1):
                # print(num, i)
                if num & (1 << i):
                    if 0 in node:
                        temp |= (1 << i)
                        node = node[0]
                    else:
                        node = node[1]
                else:
                    if 1 in node:
                        temp |= (1 << i)
                        node = node[1]
                    else:
                        node = node[0]
                        
            result = max(result, temp)
        
        return result
