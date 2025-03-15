#python 
#beats 100.00%
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        temp=[]
        k=k%n
        for i in range(n-1,n-k-1,-1):
            temp.append(nums[i])
        for j in range(n-k-1,-1,-1):
            nums[j+k]=nums[j]
        for l in range(0,len(temp)):
            nums[l]=temp[k-l-1]
