class Solution:
    def myPow(self, x: float, n: int) -> float:
             return self.quickMul(x, n) if n>=0 else 1.0/self.quickMul(x, -n)

    def quickMul(self, x, N):
        if N == 0: return 1.0
        y = self.quickMul(x, N//2)
        return y*y if N % 2 == 0 else y*y*x
