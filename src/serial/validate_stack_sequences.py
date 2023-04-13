class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stk = []
        push_i = 0
        pop_i = 0
        n_pushed = len(pushed)
        n_popped = len(popped)
        while push_i < n_pushed or pop_i < n_popped:
            if pop_i < n_popped:
                if push_i < n_pushed:
                    if stk != [] and stk[-1] == popped[pop_i]:
                        stk.pop()
                        pop_i += 1
                    else:
                        stk.append(pushed[push_i])
                        push_i += 1
                else:
                    if stk[-1] == popped[pop_i]:
                        stk.pop()
                        pop_i += 1
                    else:
                        return False
            else:
                return True
        return True
