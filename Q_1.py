#Two Sum
#Arrays
#return indices of the two numbers such that they add up to target.

class Solution(object):
    def twoSum(self, nums, target):
        for i in range (len(nums)):
            for j in range (i+1,len(nums)):
                if (nums[i] + nums[j] == target):
                    return [i, j]
        return []
