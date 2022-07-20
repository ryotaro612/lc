# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# [1, 3, 3, 1, 3, 3, 3, 2]
# [1, 3, 3, 1]
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        length = self.countLength(head)
        time = 1
        count = 0
        while True:
            left, right = head, head
            for _ in range(time):
                right = right.next
            if left.val <= right.val:
                head = left
            else:
                head = right
            count_move_left, count_move_right = 0, 0
            prev = ListNode(0, None)
            # print('start', left.val, right.val)
            while True:
                move_left, move_right = False, False
                if count_move_left < time:
                    if right is not None and count_move_right < time:
                        if left.val <= right.val:
                            move_left = True
                        else:
                            move_right = True
                    else: # count_move_right >= time
                        move_left = True
                else: # count-move_left >= time
                    if count_move_right < time and right is not None:
                        move_right = True
                
                if move_left:
                    prev.next = left
                    prev = prev.next
                    left = left.next
                    count_move_left += 1
                elif move_right:
                    # print(prev.val, right.val, '!!!', head.val)
                    prev.next = right
                    prev = prev.next
                    right = right.next
                    count_move_right += 1
                else:
                    if right is None:
                        if count_move_left + count_move_right == length:
                            # self.debug(head)
                            tail = head
                            for _ in range(length-1):
                                tail = tail.next
                            tail.next = None
                            return head
                        else:
                            time *= 2
                            prev.next = None
                            """
                            self.debug(head)
                            print('------')
                            """
                            break
                    else:
                        left = right
                        ok = False
                        for _ in range(time):
                            if right is None:
                                ok = True
                                break
                            right = right.next
                        if ok:
                            time *= 2
                            prev.next = left
                            # self.debug(head)
                            break
                        count_move_left, count_move_right = 0, 0
                """
                if count > 35:
                    raise RuntimeError()
                else:
                    print('move_left:', move_left, 'move_right:', move_right, 'prev_val:', prev.val, 'left:', left.val if left else None, 'right:', right.val if right else None, 'count_left:', count_move_left, 'count_right:', count_move_right)
                    self.debug(head)
                    count += 1
                """
    
    def countLength(sel, head):
        result = 0
        while head:
            result += 1
            head = head.next
        return result
    
    def debug(self, node):
        count = 0
        res = []
        while node:
            res.append(node.val)
            node = node.next
            count += 1
            if count > 10:
                break
        print(res)


        
