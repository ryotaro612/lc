# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = sentinel = ListNode(0, head)
        prefix_sum = dict()
        cur_sum = 0
        
        while node:
            cur_sum += node.val
            if cur_sum not in prefix_sum:
                prefix_sum[cur_sum] = node
            else:
                remove_node = prefix_sum[cur_sum].next
                remove_sum = cur_sum + remove_node.val
                prefix_sum[cur_sum].next = node.next
                while remove_node != node:
                    del prefix_sum[remove_sum]
                    remove_sum += remove_node.next.val
                    remove_node = remove_node.next
                
            node = node.next
                
        return sentinel.next
