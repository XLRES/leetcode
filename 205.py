class Solution :
    def isIsomorphic(self, s, t):
        import itertools
        maptable={}
        for c1,c2 in itertools.izip(s,t):
            if c1 in maptable :
                if maptable[c1] != c2: return False
            else: maptable[c1] = c2
        return True


S = Solution()
s = 'ab'
t = 'aa'
print S.isIsomorphic(s,t) and S.isIsomorphic(t,s)

