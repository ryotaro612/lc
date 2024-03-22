class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        cache = dict()
        return self.rec(boxes, 0, len(boxes), 0, cache)

    def rec(self, boxes, left, right, acc, cache):
        if (left, right, acc) in cache:
            return cache[(left, right, acc)]
        if left >= right:
            return 0
        
        result = 0
        peek = left
        while peek < right and boxes[peek] == boxes[left]:
            peek += 1
        
        next_acc = acc + peek - left
        result = next_acc * next_acc + self.rec(boxes, peek, right, 0, cache)
        
        for m in range(peek, right):
            if boxes[left] == boxes[m]:
                result = max(result, self.rec(boxes, m, right, next_acc, cache) + self.rec(boxes, peek, m, 0, cache))
        cache[(left, right, acc)] = result
        return result
