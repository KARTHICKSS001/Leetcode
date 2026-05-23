class Solution:
    def addBinary(self, a: str, b: str) -> str:
        dec1=int(a,2)
        dec2=int(b,2)
        add=dec2+dec1
        sum=str(bin(add)[2:])
        return sum
