#python 
#beats 19.67%
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        maxm=0
        for i in range(len(nums)):
            if (nums[i]==1):
                count+=1
                maxm=max(maxm,count)
            else:
                count=0
        return maxm
