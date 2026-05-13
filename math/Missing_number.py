class Solution:
    def missingNumber(self, nums):
        n = len(nums)

        # Expected sum of numbers from 0 to n
        expected_sum = n * (n + 1) // 2

        # Sum of elements in the array
        actual_sum = sum(nums)

        # Missing number
        return expected_sum - actual_sum


