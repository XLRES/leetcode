class Solution:
    def isHappy(self, n):
        s = 0
        numlist = []
        while (n != 1 and not n in numlist):
            numlist.append (n)
            while (n > 0):
                s += (n % 10)**2
                n /= 10
            n = s
            s = 0
        if n == 1: return True
        else: return False

S = Solution()
print S.isHappy(19)
