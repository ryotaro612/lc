import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        """
        answer
        heap =[]
        """
        node = head
        vals = []
        while node:
            vals.append(node.val)
            node = node.next

        answer = [0] * len(vals)
        heap = []
        
        for i, val in enumerate(vals):
            while heap:
                if heap[0][0] < val:
                    answer[heap[0][1]] = val
                    heapq.heappop(heap)
                else:
                    break
            heapq.heappush(heap, [val, i])
        return answer
