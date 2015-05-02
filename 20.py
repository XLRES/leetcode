class Solution:
    def isValid(self, s):
        stk = []
        for c in s:
            if len(stk) > 0:
                if c == ')' and stk[-1] == '(' : stk.pop()
                elif c == ']' and stk[-1] == '[': stk.pop()
                elif c == '}' and stk[-1] == '{': stk.pop()
                else: stk.append(c);
            else: stk.append(c)
            print stk
        if len(stk) == 0: return True
        else : return False

S = Solution()
print S.isValid("([)")
