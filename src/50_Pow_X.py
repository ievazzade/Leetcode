class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1.0 / x
            n *= -1
        ans = 1
        for i in range(n):
            ans *= x
        return ans