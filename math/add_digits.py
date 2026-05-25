class Solution:
    def addDigits(self, num: int) -> int:
        lst = list(map(int, str(num)))
        while len(lst)>1:
            n=sum(lst)
            lst = list(map(int, str(n)))
        return lst[0]
