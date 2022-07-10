# link: https://leetcode.com/problems/minimum-non-zero-product-of-the-array-elements/submissions/

class Solution:
    def minNonZeroProduct(self, p: int) -> int:

        MOD = 1000000007
        def myPow( x, n):
            if n < 0:
                x = 1/x
            n = abs(n)
            if n == 0:
                return 1
            temp = myPow(x,n//2)
            if n%2 == 0:
                return temp*temp % MOD
            else:
                return x*temp*temp %MOD
        num = (2**p)-1
        res = myPow(num-1,num//2)
        return res*num%(10**9+7)

