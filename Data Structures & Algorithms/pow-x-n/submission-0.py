class Solution:
    def myPow(self, x: float, n: int) -> float:

        #first set of base class

        if (n==0):
            return 1
        if (x==0):
            return 0


        def helper(x, n):
            if n==0:
                return 1
            res = helper(x*x, n//2)
            return x*res if n%2 else res
        
        res = helper(x, abs(n))

        if n>0:
            return res
        else:
            return 1/res
        