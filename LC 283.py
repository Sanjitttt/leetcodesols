#python 
#beats 85.57
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
    

        n=len(nums)
        i=0
        for j in range(0,len(nums)):
            if (nums[j]!=0):
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
