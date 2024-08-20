class Solution(object):
    def missingNumber(self, nums):
        maxim = max(nums)
        minim = min(nums)
        length = len(nums)

        act_sum = sum(nums)
        exp_sum =  (length) * (length + 1) // 2

        return exp_sum - act_sum
