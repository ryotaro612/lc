"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""
"""
[1]
0

[1,3,5]
0
"""
class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if head is None:
            node = Node(insertVal)
            node.next = node
            return node
        
        node = head
        length = 1
        small = head
        while node.next is not head:
            if node.next.val < small.val:
                small = node.next
            length += 1
            node = node.next
        node = small
        # print(node.val, length)
        for i in range(length):
            if node.val <= insertVal <= node.next.val or i == length - 1:
                new_node = Node(insertVal, node.next)
                node.next = new_node
                break
            else:
                node  = node.next
        return head
