class Solution:
    def hammingWeight(self, n):
        s = 0
        while n>0:
            s += n % 2
            n = n >> 1
        return s

s = Solution()
print s.hammingWeight(11)
