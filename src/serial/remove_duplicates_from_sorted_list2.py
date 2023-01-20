class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode()
        prev = sentinel
        node = head
        while node:
            if node.next:
                val = node.val
                if node.val == node.next.val:                  
                    while node and node.val == val:
                        node = node.next
                else:
                    prev.next = ListNode(val)
                    prev = prev.next
                    node =node.next
            else:
                prev.next = ListNode(node.val)
                node = node.next
        return sentinel.next
