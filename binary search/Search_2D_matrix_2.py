class Solution:
    def searchMatrix(self, matrix, target):
        n = len(matrix[0]) 
        for row in matrix:
            if row[0] > target or row[n-1] < target:
                continue
            low, high = 0, n - 1

            while low <= high:
                mid = (low + high) // 2

                if row[mid] == target:
                    return True
                elif row[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1

        return False
