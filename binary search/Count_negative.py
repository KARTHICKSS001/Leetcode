class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count=0
        rem=0
        for i in grid:
            for j in i:
                
                count+=1
                if j>=0:
                    rem+=1
        total=count-rem
        return total
