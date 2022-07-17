class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1.0 / x
            n *= -1
        ans = 1
        for i in range(n):
            ans *= x
        return ans

class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def fastPow(x, n):
            if n == 0:
                return 1
            half = fastPow(x, n//2)
            
            if n % 2 == 0:
                return half * half
            else:
                return half * half * x
        
        if n < 0:
            x = 1.0 / x
            n *= -1
        
        return fastPow(x, n)