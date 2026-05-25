class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1   # 2147483647
        INT_MIN = -2**31      # -2147483648
        
        sign = -1 if x < 0 else 1
        value = int(str(abs(x))[::-1]) * sign
        
        if value < INT_MIN or value > INT_MAX:
            return 0
        return value
