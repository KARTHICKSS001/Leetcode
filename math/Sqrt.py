class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2:
            return x
        right=x//2
        left=1
        while left<=right:
            mid=(left+right)//2
            square=mid * mid
            if square==x:
                return mid
            elif square<x:
                left=mid+1
            else:
                right=mid-1

        return right
