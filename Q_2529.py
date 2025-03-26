#Maximum Count of Positive Integer and Negative Integer
#Arrays

class Solution(object):
    def maximumCount(self, nums):
        neg = 0
        pos=0
        for i in range(len(nums)):
            if (nums[i]<0):
                neg=neg+1
            elif (nums[i]>0):
                pos=pos+1
        
        return (max(neg,pos))
