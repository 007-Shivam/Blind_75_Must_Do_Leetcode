class Solution(object):
    def longestConsecutive(self, nums):
        nums.sort()  
        prev_seq = 0
        new_seq = 0

        for i in range(len(nums) - 1):  
            if nums[i+1] == nums[i] + 1:
                new_seq += 1
            elif nums[i+1] != nums[i]:  
                prev_seq = max(prev_seq, new_seq)
                new_seq = 0
                
        return max(new_seq, prev_seq) + 1 if nums else 0   
