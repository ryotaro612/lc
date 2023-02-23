class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        stack, order = [], []
        
        for num in preorder:
            if stack:
                if num < stack[-1]:
                    stack.append(num)
                else: # stack[-1] < num
                    while stack and stack[-1] < num:
                        order.append(stack.pop())
                    stack.append(num)
            else:
                stack.append(num)
        while stack:
            order.append(stack.pop())
        return order == sorted(order)
