# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:

        while True:
            head, found = self.remove_consec(head)
            if not found:
                return head
        
    def remove_consec(self, head):
        """
        prefix_sum_d = dict()
        pref
        """
        node = head
        nodes = []
        while node:
            nodes.append(node)
            node = node.next
        
        if [node for node in nodes if node.val == 0]:
            return self.build_list([node for node in nodes if node.val]), True
        
        prefix_sum = {0: -1}
        current_sum = 0
        for i, node in enumerate(nodes):
            current_sum += node.val
            if current_sum in prefix_sum:
                result = nodes[:prefix_sum[current_sum]+1] + nodes[i+1:]
                return self.build_list(result), True
            prefix_sum[current_sum] = i
        return head, False

    def build_list(self, nodes):
        sentinel = ListNode()
        cur = sentinel
        for node in nodes:
            cur.next = node
            cur = node
        cur.next = None
        return sentinel.next
