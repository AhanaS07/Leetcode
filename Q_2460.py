#Apply Operations to an Array
#Arrays
#If nums[i] == nums[i + 1], then multiply nums[i] by 2 and set nums[i + 1] to 0. Otherwise, you skip this operation.

class Solution(object):
    def applyOperations(self, nums):
        for i in range(len(nums)-1):
            if (nums[i] == nums[i+1]):
                nums[i] = nums[i]*2
                nums[i+1] = 0

        mod_n = [num for num in nums if num!=0]
        zct = len(nums) - len(mod_n)
   
        return mod_n + ([0]*zct)
