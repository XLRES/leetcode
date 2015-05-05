class Solution:
    def countPrimes(self, n):
        import math
        if n <= 2 : return 0
        half = n / 2;
        sn = (int)(math.sqrt(n))
        p = []
        for i in range (half):
            p.append (True)
        for i in range (sn):
            if p[i]:
                for j in range(2 * i * i + 6 * i + 3 , half , 2 * i + 3):
                    p[j] = False
        
        count = 1
        for i in range(half - 1):
            if p[i]:
                count += 1
        return count

S = Solution()
for i in range (100):
    print i, S.countPrimes(i)
