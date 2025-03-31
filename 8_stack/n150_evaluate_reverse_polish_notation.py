class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for v in tokens: #O(n)
            if v not in '+-/*': #O(1)
                stack.append(v)
            else:
                a=int(stack.pop())
                b=int(stack.pop())
                if v=='+':    
                    stack.append(a+b)
                elif v=='*':
                    stack.append(a*b)
                elif v=='-':
                    stack.append(b-a)
                else:
                    stack.append(b/a)       
        return int(stack[-1]) #O(n)