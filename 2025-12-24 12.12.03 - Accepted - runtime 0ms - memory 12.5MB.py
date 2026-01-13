class Solution(object):
    def commonFactors(self, a, b):
        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x
        g = gcd(a, b)
        count = 0
        for i in range(1, g + 1):
            if g % i == 0:
                count += 1
        return count