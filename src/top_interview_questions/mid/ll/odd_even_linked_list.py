# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
[1 2 3 4 5 6 7 8]
 i j 
[1 3 2 4 5 6 7 8]
   i   j  
[1 3 5 2 4 6 7 8]
     i     j
[1 3 5 7 2 4 6 8]
"""
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        i, j = head, head.next
        
        while j and j.next:
            # odd = 5
            odd = j.next
            # i_next = 2
            i_next = i.next
            # j_next = 6
            j_next = j.next.next
            # i.next = 5
            i.next = odd
            odd.next = i_next # 2
            # 6
            j.next = j_next
            i = i.next
            j = j.next
        return head
"""
public class Solution {
public ListNode oddEvenList(ListNode head) {
    if (head != null) {
    
        ListNode odd = head, even = head.next, evenHead = even; 
    
        while (even != null && even.next != null) {
            odd.next = odd.next.next; 
            even.next = even.next.next; 
            odd = odd.next;
            even = even.next;
        }
        odd.next = evenHead; 
    }
    return head;
}}
"""   
